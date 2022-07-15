import 'package:flutter/material.dart';


class TelaSearchingJob extends StatefulWidget {
  const TelaSearchingJob({Key? key}) : super(key: key);

  @override
  State<TelaSearchingJob> createState() => _TelaSearchingJobState();
}

class _TelaSearchingJobState extends State<TelaSearchingJob> {

  List _itens = [];

  void _carregarItens(){

    _itens = [];
    for(int i=0; i<=10; i++){

      Map<String, dynamic> item = Map();
      item["titulo"] = "Título ${i} Lorem ipsum dolor sit amet.";
      item["descricao"] = "Descrição ${i} ipsum dolor sit amet.";
      _itens.add( item );

    }

  }

  final ScrollController _scrollController = ScrollController();

  @override
  Widget build(BuildContext context) {

    var _colorHomeButton = Colors.white;
    var _colorCleaningButton = Colors.white;
    var _colorPoolButton = Colors.white;
    var _colorPartyButton = Colors.white;
    var _colorOthersButton = Colors.white;

    _carregarItens();

    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.teal,
        title: const Text("Searching Job"),
      ),
      body: Container(
        child: SingleChildScrollView(
          child: Column(
            children: [
              const Padding(
                  padding: EdgeInsets.only(top: 32, left: 24, right: 24),
                  child: TextField(
                    showCursor: false,
                    keyboardType: TextInputType.text,
                    decoration: InputDecoration(
                        hintText: "Search Job",
                        suffixIcon: Icon(Icons.search),
                        suffixIconColor: Colors.blueGrey,
                        enabledBorder: UnderlineInputBorder(
                            borderSide: BorderSide(color: Colors.blueGrey)
                        ),
                        focusedBorder: UnderlineInputBorder(
                            borderSide: BorderSide(color: Colors.teal)
                        )
                    ),
                  )
              ),
              Padding(
                  padding: const EdgeInsets.only(top: 8, left: 24, right: 24),
                  child: SingleChildScrollView(
                    scrollDirection: Axis.horizontal,
                    child: Row(
                      children: [
                        OutlineButton(
                          color: Colors.red,
                          shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(20)
                          ),
                          child: const Text(
                            "Home",
                            style: TextStyle(
                              color: Colors.black54,
                              fontSize: 18,
                            ),
                          ),
                          onPressed: (){
                            _colorHomeButton = Colors.red;
                          },
                        ),
                        OutlineButton(
                          shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(20)
                          ),
                          child: const Text(
                            "Cleaning",
                            style: TextStyle(
                              color: Colors.black54,
                              fontSize: 18,
                            ),
                          ),
                          onPressed: (){},
                        ),
                        OutlineButton(
                          shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(20)
                          ),
                          child: const Text(
                            "Pool",
                            style: TextStyle(
                              color: Colors.black54,
                              fontSize: 18,
                            ),
                          ),
                          onPressed: (){},
                        ),
                        OutlineButton(
                          shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(20)
                          ),
                          child: const Text(
                            "Party",
                            style: TextStyle(
                              color: Colors.black54,
                              fontSize: 18,
                            ),
                          ),
                          onPressed: (){},
                        ),
                        OutlineButton(
                          shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(20)
                          ),
                          child: const Text(
                            "Other",
                            style: TextStyle(
                              color: Colors.black54,
                              fontSize: 18,
                            ),
                          ),
                          onPressed: (){},
                        ),
                      ],
                    ),
                  )
              ),
              Column(
                children: [
                  OutlinedButton(
                    child: const Text(
                    "This is an Outline\"d\"Button. (Not OutlineButton)",
                    style: TextStyle(color: Colors.white),
                  ),
                  onPressed: () => print("Tapped"),
                  //onPressed: null, //Uncomment this statement to check disabled state.
                  style: ButtonStyle(
                    backgroundColor: MaterialStateProperty.resolveWith<Color>((states) {
                      if (states.contains(MaterialState.disabled)) {
                        return Colors.black;
                      }
                      return Colors.blue;
                    }),
                    overlayColor: MaterialStateProperty.resolveWith<Color>((states) {
                      if (states.contains(MaterialState.pressed)) {
                        return Colors.red;
                      }
                      return Colors.transparent;
                    }),
                    side: MaterialStateProperty.resolveWith((states) {
                      Color _borderColor;

                      if (states.contains(MaterialState.disabled)) {
                        _borderColor = Colors.greenAccent;
                      } else if (states.contains(MaterialState.pressed)) {
                        _borderColor = Colors.yellow;
                      } else {
                        _borderColor = Colors.pinkAccent;
                      }

                      return BorderSide(color: _borderColor, width: 5);
                    }),
                    shape: MaterialStateProperty.resolveWith<OutlinedBorder>((_) {
                      return RoundedRectangleBorder(borderRadius: BorderRadius.circular(16));
                    }),
                  ),
                ),
                  Scrollbar(
                    child: ListView.builder(
                      padding: const EdgeInsets.only(top: 8, left: 24, right: 24),
                      shrinkWrap: true,
                      controller: _scrollController,
                      itemCount: _itens.length,
                      itemBuilder: (context, indice){
                        return ListTile(
                          title: Text( _itens[indice]["titulo"] ),
                          subtitle: Text( _itens[indice]["descricao"] ),
                        );
                      }
                    ),
                  )
                ],
              )
            ],
          ),
        ),
      ),
    );
  }
}
