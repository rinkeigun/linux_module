using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Activities;
//using System.ComponentModel.Composition;
using System.ComponentModel;
using FujiXerox.DocuWorks.Toolkit;

namespace ClassDocuworksActivity
{
    public class ChangeFirstPage: CodeActivity
    {
        [Category("Input")]
        [RequiredArgument]
        public InArgument<String> InFile { get; set; }

        [Category("Input")]
        public InArgument<String> OutFile { get; set; }

        [Category("Output")]
        public OutArgument<String> ResultNumber { get; set; }

        protected override void Execute(CodeActivityContext context)
        {
            var inFile = InFile.Get(context);
            var outFile = OutFile.Get(context);

            Xdwapi.XDW_DOCUMENT_HANDLE documentHandle = new Xdwapi.XDW_DOCUMENT_HANDLE();
            Xdwapi.XDW_OPEN_MODE_EX mode = new Xdwapi.XDW_OPEN_MODE_EX();
            mode.Option = Xdwapi.XDW_OPEN_UPDATE;
            mode.AuthMode = Xdwapi.XDW_AUTH_NODIALOGUE;
            //api_result = 
            Xdwapi.XDW_OpenDocumentHandle(outFile, ref documentHandle, mode);
            Xdwapi.XDW_DeletePage( documentHandle, 1);

            // inputPath
            Xdwapi.XDW_InsertDocument( documentHandle, 1, inFile);
            Xdwapi.XDW_SaveDocument(documentHandle);
            Xdwapi.XDW_CloseDocumentHandle(documentHandle);
        }
    }
}
