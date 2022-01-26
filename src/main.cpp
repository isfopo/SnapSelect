#include <Arduino.h>
#include <EasyButton.h>

#define MIDI_CHANNEL 1
#define HOLD_TIME 500
#define CC_THRESHOLD 64

uint8_t pins[2] = {
    0, 1};

EasyButton buttons[2] = {
    EasyButton(pins[0]),
    EasyButton(pins[1]),
};

uint8_t pressedNotes[2] = {
    0, 1};

uint8_t heldNotes[8] = {
    8, 9};

bool noteIsHeld[2] = {false, false};

void sendCC(uint8_t note)
{
  usbMIDI.sendControlChange(note, 127, MIDI_CHANNEL);
  usbMIDI.sendControlChange(note, 0, MIDI_CHANNEL);
}

void setHeld(uint8_t index)
{
  noteIsHeld[index] = true;
}

void setup()
{
  for (int i = 0; i < 2; i++)
  {
    buttons[i].begin();
  }

  buttons[0].onPressed([]() -> void
                       { sendCC(pressedNotes[0]); });

  buttons[1].onPressed([]() -> void
                       { sendCC(pressedNotes[1]); });

  buttons[0].onPressedFor(HOLD_TIME, []() -> void
                          { setHeld(0); });

  buttons[1].onPressedFor(HOLD_TIME, []() -> void
                          { setHeld(1); });
}

void loop()
{
  usbMIDI.read();

  for (int i = 0; i < 2; i++)
  {
    buttons[i].read();

    if (buttons[i].wasReleased() && noteIsHeld[i])
    {
      sendCC(heldNotes[i]);
      noteIsHeld[i] = false;
    }
  }
}