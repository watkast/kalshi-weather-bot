# Range-Scalp Bot

*Updated Wed Nov 04 11:47 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47207 | 41112 | 6095 (72) | 3 | $-13566.63 | -4.6% |
| **+10¢** | 35265 | 28195 | 7070 (97) | 4 | $-12388.96 | -5.6% |
| **+15¢** | 29529 | 21916 | 7613 (125) | 4 | $-11359.72 | -6.1% |
| **+20¢** | 26232 | 18258 | 7974 (165) | 4 | $-10020.79 | -6.1% |
| **+10¢ (15¢ stop)** | 57533 | 57440 | 93 (56) | 3 | $-21454.44 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 11:47 | +10 stop | BTC | UP | 0.55 | open |  |
| 11-04 11:47 | +20 | BTC | UP | 0.55 | open |  |
| 11-04 11:47 | +15 | BTC | UP | 0.55 | open |  |
| 11-04 11:47 | +10 | BTC | UP | 0.55 | open |  |
| 11-04 11:47 | +5 | BTC | UP | 0.55 | open |  |
| 11-04 11:46 | +10 stop | ZEC | UP | 0.61 | 0.45 | -1.95 |
| 11-04 11:46 | +20 | ZEC | UP | 0.61 | open |  |
| 11-04 11:46 | +15 | ZEC | UP | 0.61 | open |  |
| 11-04 11:46 | +10 | ZEC | UP | 0.61 | open |  |
| 11-04 11:46 | +5 | ZEC | UP | 0.61 | open |  |
| 11-04 11:46 | +10 stop | HYPE | UP | 0.51 | open |  |
| 11-04 11:46 | +20 | HYPE | UP | 0.51 | open |  |
| 11-04 11:46 | +15 | HYPE | UP | 0.51 | open |  |
| 11-04 11:46 | +10 | HYPE | UP | 0.51 | open |  |
| 11-04 11:46 | +5 | HYPE | UP | 0.51 | 0.56 | 0.14 |
| 11-04 11:46 | +10 stop | BNB | UP | 0.69 | open |  |
| 11-04 11:46 | +20 | BNB | UP | 0.69 | open |  |
| 11-04 11:46 | +15 | BNB | UP | 0.69 | open |  |
| 11-04 11:46 | +10 | BNB | UP | 0.69 | open |  |
| 11-04 11:46 | +5 | BNB | UP | 0.69 | open |  |
| 11-04 11:43 | +10 stop | ETH | DOWN | 0.38 | 0.54 | 1.25 |
| 11-04 11:43 | +10 stop | SOL | UP | 0.60 | 0.26 | -3.71 |
| 11-04 11:43 | +20 | SOL | UP | 0.60 | 0.81 | 1.82 |
| 11-04 11:43 | +15 | SOL | UP | 0.60 | 0.75 | 1.19 |
| 11-04 11:43 | +10 | SOL | UP | 0.59 | 0.75 | 1.29 |
| 11-04 11:43 | +5 | SOL | UP | 0.59 | 0.75 | 1.29 |
| 11-04 11:41 | +10 stop | ETH | UP | 0.48 | 0.27 | -2.42 |
| 11-04 11:41 | +10 stop | ETH | DOWN | 0.42 | 0.58 | 1.24 |
| 11-04 11:40 | +10 stop | BTC | DOWN | 0.67 | 0.52 | -1.84 |
| 11-04 11:40 | +10 stop | SOL | UP | 0.59 | 0.78 | 1.60 |
| 11-04 11:40 | +5 | SOL | UP | 0.58 | 0.78 | 1.69 |
| 11-04 11:39 | +5 | SOL | UP | 0.49 | 0.55 | 0.24 |
| 11-04 11:39 | +10 stop | NEAR | UP | 0.70 | 0.83 | 1.05 |
| 11-04 11:39 | +20 | NEAR | UP | 0.70 | 0.93 | 2.05 |
| 11-04 11:39 | +15 | NEAR | UP | 0.70 | 0.86 | 1.36 |
| 11-04 11:39 | +10 | NEAR | UP | 0.71 | 0.83 | 0.95 |
| 11-04 11:39 | +5 | NEAR | UP | 0.71 | 0.83 | 0.95 |
| 11-04 11:38 | +10 | BTC | UP | 0.64 | no | -6.57 |
| 11-04 11:38 | +5 | BTC | UP | 0.64 | no | -6.57 |
| 11-04 11:38 | +10 stop | XRP | UP | 0.70 | 0.49 | -2.43 |
