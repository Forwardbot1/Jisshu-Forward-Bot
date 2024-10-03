echo "Cloning Repo...."
if [ -z $BRANCH ]
then
  echo "Cloning main branch...."
  git clone https://github.com/Jisshubot/Jisshu-forward-bot Jisshubot/Jisshu-forward-Bot 
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/Jisshubot/Jisshu-forward-bot -b $BRANCH /Jisshu-forward-Bot
fi
cd Jisshubot/Jisshu-forward-Bot 
pip3 install -U -r requirements.txt
echo "Starting Bot...."
gunicorn app:app & python3 main.py
