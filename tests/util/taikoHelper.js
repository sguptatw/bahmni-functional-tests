const { button, toRightOf, textBox, into, write, click, timeField,below, checkBox,waitFor,image,within } = require('taiko');
var date = require("./date");

async function executeConfigurations(configurations){
    for(var configuration of configurations){
        switch(configuration.type) {
            case 'Group':
                await executeConfigurations(configuration.value)
              break;
            case 'TextArea':
                if(configuration.proximity!=null&&configuration.proximity!="")
                {
                    switch(configuration.proximity){
                        case 'below':
                            await write(configuration.value,into(textBox(below(configuration.proximityLabel), toRightOf(configuration.label))))
                        break;
                        case 'above':
                            await write(configuration.value,into(textBox(below(configuration.proximityLabel), toRightOf(configuration.label))))
                        break;
                        default:
                                console.log("Unhandled "+configuration.label+":"+configuration.value)
                            break;
                    }
                }
                else
                    await write(configuration.value,into(textBox(toRightOf(configuration.label))))
              break;
            case 'TextBox':
                await write(configuration.value,into(textBox(toRightOf(configuration.label))))
            break;
          case 'Button':
                await click(button(configuration.value),toRightOf(configuration.label))
            break;      
            case 'Date':
                if(configuration.value=='Today')
                    await timeField({type:"date"},toRightOf(configuration.label)).select(date.today());
                else
                {
                    dateLessThan = configuration.value.split("-");
                    if(dateLessThan.length>1)
                    {
                        await timeField({type:"date"},toRightOf(configuration.label)).select(date.getDateAgo(dateLessThan[1]));
                    }
                }
            break;      
            default:
                console.log("Unhandled "+configuration.label+":"+configuration.value)
          }            
    }
}

module.exports={
    executeConfigurations:executeConfigurations,
}