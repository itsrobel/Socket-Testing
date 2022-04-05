from transformers import AutoModelForCausalLM, AutoTokenizer
import torch



# Let's chat for 5 lines


class Leo:
    def __init__(self, user, history):
        self.user = user
        self.history = history
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
        self.model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
        self.step = 0

    def Message(self,msg):

    # encode the new user input, add the eos_token and return a tensor in Pytorch
        new_user_input_ids = self.tokenizer.encode(msg+self.tokenizer.eos_token, return_tensors='pt')

    # append the new user input tokens to the chat history
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if self.step > 0 else new_user_input_ids

    # generated a response while limiting the total chat history to 1000 tokens,
        chat_history_ids = self.model.generate(bot_input_ids,
                                      max_length=1000,
                                      do_sample=True,
                                      top_p=0.95,
                                      top_k=0,
                                      temperature=0.75,
                                      pad_token_id=self.tokenizer.eos_token_id
                                      )

    # pretty print last ouput tokens from bot
        self.step+=1
        return self.tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        # print("DialoGPT: {}".format()
