#include <Arduino.h>
#include <EasyButton.h>

#define MIDI_CHANNEL 1

uint8_t pins[2] = {
    0, 1};

EasyButton buttons[2] = {
    EasyButton(pins[0]),
    EasyButton(pins[1]),
};

uint8_t pressedNotes[2] = {
    0, 1};

bool noteIsHeld[2] = {false, false};

void sendNote(uint8_t note)
{
  usbMIDI.sendNoteOn(note, 127, MIDI_CHANNEL);
  usbMIDI.sendNoteOff(note, 0, MIDI_CHANNEL);
}

void setup()
{
  for (int i = 0; i < 2; i++)
  {
    buttons[i].begin();
  }

  buttons[0].onPressed([]() -> void
                       { sendNote(pressedNotes[0]); });

  buttons[1].onPressed([]() -> void
                       { sendNote(pressedNotes[1]); });
}

void loop()
{
  usbMIDI.read();

  for (int i = 0; i < 2; i++)
  {
    buttons[i].read();
  }
}