rm *.db
#. setup_venv.sh
python create_db.py

echo "*********************************"
echo "*  KILLING ANY PROCESS          *"
echo "*  Using Port 5023              *"
echo "*                               *"
echo "*********************************"

# for i in *.ipynb; do cp ${i} bozo.ipynb && papermill bozo.ipynb ${i} && jupyter nbconvert --output-dir='./database_analysis_html_output' ${i} --to html && rm -rf bozo.ipynb;
#     [[ -f  "$i" ]] || continue
# done

pid_to_kill=$(lsof -t -i :5023 -s TCP:LISTEN)


if ! [ -z "$pid_to_kill" ];
then
  sudo lsof -ti tcp:5023 | xargs kill
fi

#for pid_to_kill in $(lsof -t -i :5023 -s TCP:LISTEN); do sudo kill ${pid_to_kill};


python app.py > /dev/null &
#python app.py  &

echo "***********************************"
echo "* Access Flask at the following   *"
echo "* Address                         *"
echo "* http://127.0.0.1:5023           *"
echo "*                                 *"
echo "***********************************"

read -p "Press enter to kill flask application:"
