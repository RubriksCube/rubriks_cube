# Instructions

You are a helpful, pattern-following assistant. Use the following instructions to respond to user inputs.
1. Start your answer with a prefix that says "The right answer is: ".
2. Explain the response given in Step 1, with a prefix that says "Because: ". The explanation should not just paraphrase or include what is already mentioned in the user input.
3. Show all the answer choices with their numeric probability of being the correct answer

## Examples

Please choose the most plausible ending (event) for the given context. There is only **one** correct answer. After selecting a correct answer, explain why you selected that option. The examples do not include an explanation but you will need to provide it when answering the question.

For reference, we provide below four examples that have already been solved for you.

**Example 1**
Context: [header] How to remove pen marks [title] Treat the stain as quickly as possible. [step] The longer you let the ink sit in the fabric, the harder it will be to remove, so take action as soon as you notice the stain. Ideally, the ink will still be wet when you treat the fabric.

Question: Choose the option that best completes the above story.

Options:

A. Dab the spot with a cloth or paper towel to help speed up the process. [substeps] If there is any sticky residue, it will solidify over time and will not help with picking the ink out of the fabric.
B. [title] Apply a pre-wash treatment solution. [step] There are a wide variety of pre-wash treatments available in the cleaning aisle of the grocery store, where you purchase laundry detergent and dryer sheets.
C. If stains remain after treatment, wash your fabric with water and blot out any excess ink. [substeps] Keep over-the-counter stain removers on hand even if you only were able to get it out with a professional stain remover.
D. One of the first things you'll need to do is immediately treat and let the fabric dry to a temperature comfortable for you. If you are in a rush, wait until the stain is completely gone before calling for a professional to finish it off.

Answer: B

**Example 2**
Context: [header] How to fix fluorescent light humming [title] Unplug the unit or flip the breaker off if it is directly plugged into the wall. [step] If the light is permanently connected to power, shut off the breaker. Do not disassemble the unit without disconnecting power.

Question: Choose the option that best completes the above story.

Options:

A. [substeps] Even if you have wireless or mono-fi services within the home, operate the unit without power. If you have an internet connection, disconnect it now.
B. [title] Use a screwdriver to cut the power supply to the unit. [step] Carefully carefully cut into the back of the light housing near the power supply and switch.
C. [title] Remove fluorescent tubes and set safely aside. [step] Make sure you don't break them\! You can put them off to the side.
D. [title] Remove the incandescent burner. [step] Most incandescent-powered light fixtures will have some hand-operated power adapters which you can purchase at a hardware store.

Answer: C

**Example 3**
Context: [header] How to care for an angelfish [title] Choose the right size tank. [step] Even if your angelfish is small now, it will grow. Angelfish can grow to be about 6 inches long and 8 inches tall.

Question: Choose the option that best completes the above story.

Options:

A. If your angelfish is larger than 8 inches, you should instead choose a size less than 8 inches. Begin by arranging the aquarium table or bowl so that the yellow side faces up.
B. A large tank is ideal, with room for one to two gallons per 10 gallons (19 l) of water. [substeps] Angelfish should be able to crawl, hop, and swim without much trouble.
C. With proper aquarium care, your angelfish should be a healthy size. As with any other fish, this area should be ventilated and allow easy access for them to dive and play.
D. When selecting a tank, make sure it's at least 55 gallons in capacity. If you can afford a tank bigger than this, and fit it in your home, bigger is always preferred.

Answer: D

**Example 4**
Context: [header] How to clean mirrors [title] Assess the condition of your mirror. [step] Depending on the location and use of your mirror, it may have accumulated special kinds of grime that need specific cleaning agents to remove. Limescale or calcium deposits are likely culprits, and should be pre-treated before you tackle lesser stains.

Question: Choose the option that best completes the above story.

Options:

A. You can : [substeps] Identify calcium deposits by white, slightly rough textured spots. These can be removed by white vinegar on a damp cloth.
B. White-or wax-based stains tend to be easier to spot than brass or copper stains, but you should never leave the mirror polished. Ideally, your mirror should appear spotless.
C. [substeps] If the material of your mirror reflects sunlight, washing it with a water-based detergent should be safe for the mirror. Darker colors won't mesh well with darker finishes, so take it to an oil-based " should " or " ought " cleaner.
D. If more severe stains are present, such as one that won't lift, then your best bet is to hire a professional to clean them for you. By doing so, you'll also be able to figure out what's causing them.

Answer: A

## Exercise

Context: {{ctx_a}}

Question: Choose the option that best completes the above story.

Options:

A. {{ctx_b}} {{endings[0]}}
B. {{ctx_b}} {{endings[1]}}
C. {{ctx_b}} {{endings[2]}}
D. {{ctx_b}} {{endings[3]}}
