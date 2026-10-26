# Range-Scalp Bot

*Updated Mon Oct 26 12:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34813 | 30394 | 4419 (43) | 5 | $-9652.32 | -4.4% |
| **+10¢** | 26054 | 20944 | 5110 (65) | 5 | $-8452.30 | -5.2% |
| **+15¢** | 21799 | 16297 | 5502 (89) | 6 | $-7563.42 | -5.5% |
| **+20¢** | 19320 | 13552 | 5768 (112) | 7 | $-6668.05 | -5.5% |
| **+10¢ (15¢ stop)** | 42610 | 42548 | 62 (33) | 4 | $-16188.59 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 12:37 | +10 | DOGE | DOWN | 0.69 | open |  |
| 10-26 12:36 | +5 | DOGE | DOWN | 0.68 | open |  |
| 10-26 12:36 | +10 stop | NEAR | UP | 0.54 | open |  |
| 10-26 12:36 | +10 stop | DOGE | DOWN | 0.67 | open |  |
| 10-26 12:36 | +10 stop | BTC | DOWN | 0.70 | open |  |
| 10-26 12:35 | +10 stop | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 10-26 12:35 | +10 stop | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 10-26 12:35 | +10 stop | XRP | UP | 0.65 | 0.43 | -2.54 |
| 10-26 12:35 | +10 stop | ZEC | UP | 0.61 | 0.74 | 0.99 |
| 10-26 12:35 | +10 stop | HYPE | UP | 0.62 | open |  |
| 10-26 12:35 | +10 stop | DOGE | UP | 0.52 | 0.68 | 1.26 |
| 10-26 12:35 | +10 stop | BTC | UP | 0.51 | 0.62 | 0.75 |
| 10-26 12:34 | +10 stop | BNB | DOWN | 0.58 | 0.68 | 0.66 |
| 10-26 12:34 | +20 | BNB | DOWN | 0.59 | 0.80 | 1.81 |
| 10-26 12:34 | +15 | BNB | DOWN | 0.59 | 0.76 | 1.40 |
| 10-26 12:34 | +10 | BNB | DOWN | 0.60 | 0.73 | 0.99 |
| 10-26 12:34 | +5 | BNB | DOWN | 0.59 | 0.68 | 0.57 |
| 10-26 12:34 | +10 stop | HYPE | UP | 0.67 | 0.41 | -2.93 |
| 10-26 12:33 | +10 stop | ETH | DOWN | 0.59 | 0.42 | -2.05 |
| 10-26 12:33 | +20 | ETH | DOWN | 0.60 | 0.82 | 1.92 |
| 10-26 12:33 | +15 | ETH | DOWN | 0.60 | 0.82 | 1.92 |
| 10-26 12:33 | +10 | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 10-26 12:33 | +5 | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 10-26 12:33 | +5 | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-26 12:33 | +10 stop | DOGE | DOWN | 0.59 | 0.36 | -2.64 |
| 10-26 12:33 | +20 | DOGE | DOWN | 0.59 | open |  |
| 10-26 12:33 | +15 | DOGE | DOWN | 0.59 | open |  |
| 10-26 12:33 | +10 | DOGE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-26 12:33 | +5 | DOGE | DOWN | 0.59 | 0.64 | 0.16 |
| 10-26 12:33 | +10 stop | ZEC | DOWN | 0.57 | 0.37 | -2.35 |
| 10-26 12:33 | +5 | BTC | DOWN | 0.69 | 0.78 | 0.62 |
| 10-26 12:33 | +10 stop | HYPE | DOWN | 0.67 | 0.37 | -3.33 |
| 10-26 12:32 | +10 stop | XRP | UP | 0.61 | 0.71 | 0.68 |
| 10-26 12:32 | +10 stop | ZEC | UP | 0.44 | 0.54 | 0.64 |
| 10-26 12:32 | +5 | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 10-26 12:32 | +10 stop | BNB | DOWN | 0.56 | 0.67 | 0.76 |
| 10-26 12:32 | +20 | BNB | DOWN | 0.56 | 0.77 | 1.79 |
| 10-26 12:32 | +15 | BNB | DOWN | 0.56 | 0.77 | 1.79 |
| 10-26 12:32 | +10 | BNB | DOWN | 0.56 | 0.67 | 0.76 |
| 10-26 12:32 | +5 | BNB | DOWN | 0.56 | 0.63 | 0.35 |
