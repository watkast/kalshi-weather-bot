# Range-Scalp Bot

*Updated Sat Oct 31 10:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42134 | 36761 | 5373 (55) | 3 | $-11824.03 | -4.5% |
| **+10¢** | 31414 | 25194 | 6220 (79) | 2 | $-10573.60 | -5.4% |
| **+15¢** | 26266 | 19560 | 6706 (107) | 4 | $-9667.95 | -5.9% |
| **+20¢** | 23326 | 16303 | 7023 (138) | 4 | $-8505.55 | -5.8% |
| **+10¢ (15¢ stop)** | 51387 | 51312 | 75 (41) | 0 | $-19388.69 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 10:42 | +10 stop | BNB | DOWN | 0.71 | 0.47 | -2.73 |
| 10-31 10:42 | +15 | BNB | DOWN | 0.66 | open |  |
| 10-31 10:42 | +10 | BNB | DOWN | 0.66 | 0.79 | 1.02 |
| 10-31 10:42 | +5 | BNB | DOWN | 0.66 | 0.73 | 0.40 |
| 10-31 10:42 | +10 stop | HYPE | UP | 0.37 | 0.68 | 2.77 |
| 10-31 10:41 | +10 stop | XRP | DOWN | 0.65 | 0.79 | 1.12 |
| 10-31 10:37 | +10 stop | XRP | DOWN | 0.48 | 0.75 | 2.38 |
| 10-31 10:37 | +10 stop | SOL | DOWN | 0.57 | 0.75 | 1.48 |
| 10-31 10:37 | +10 stop | XRP | UP | 0.59 | 0.40 | -2.24 |
| 10-31 10:36 | +10 stop | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-31 10:36 | +10 stop | BNB | DOWN | 0.57 | 0.67 | 0.66 |
| 10-31 10:35 | +10 stop | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-31 10:35 | +10 stop | XRP | DOWN | 0.60 | 0.45 | -1.85 |
| 10-31 10:35 | +15 | HYPE | UP | 0.70 | open |  |
| 10-31 10:35 | +10 | HYPE | UP | 0.70 | open |  |
| 10-31 10:35 | +5 | HYPE | UP | 0.70 | open |  |
| 10-31 10:35 | +20 | HYPE | UP | 0.70 | open |  |
| 10-31 10:34 | +5 | DOGE | UP | 0.63 | 0.76 | 1.00 |
| 10-31 10:34 | +10 stop | ZEC | DOWN | 0.47 | 0.27 | -2.27 |
| 10-31 10:33 | +10 stop | NEAR | DOWN | 0.53 | 0.66 | 0.96 |
| 10-31 10:33 | +10 stop | XRP | UP | 0.56 | 0.39 | -2.05 |
| 10-31 10:33 | +10 | XRP | UP | 0.57 | open |  |
| 10-31 10:33 | +10 stop | HYPE | UP | 0.67 | 0.48 | -2.24 |
| 10-31 10:33 | +10 | HYPE | UP | 0.62 | 0.72 | 0.69 |
| 10-31 10:33 | +10 stop | DOGE | UP | 0.59 | 0.76 | 1.40 |
| 10-31 10:33 | +20 | DOGE | UP | 0.59 | 0.79 | 1.71 |
| 10-31 10:33 | +15 | DOGE | UP | 0.60 | 0.76 | 1.32 |
| 10-31 10:33 | +10 | DOGE | UP | 0.60 | 0.76 | 1.32 |
| 10-31 10:33 | +5 | DOGE | UP | 0.59 | 0.64 | 0.16 |
| 10-31 10:32 | +10 stop | ZEC | DOWN | 0.50 | 0.63 | 0.95 |
| 10-31 10:32 | +5 | XRP | UP | 0.60 | open |  |
| 10-31 10:32 | +10 stop | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-31 10:32 | +20 | ETH | DOWN | 0.63 | 0.86 | 2.04 |
| 10-31 10:32 | +15 | ETH | DOWN | 0.63 | 0.80 | 1.41 |
| 10-31 10:32 | +10 | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-31 10:32 | +5 | ETH | DOWN | 0.63 | 0.71 | 0.48 |
| 10-31 10:32 | +5 | HYPE | UP | 0.66 | 0.72 | 0.29 |
| 10-31 10:32 | +10 stop | SOL | UP | 0.70 | 0.37 | -3.62 |
| 10-31 10:32 | +5 | SOL | UP | 0.70 | open |  |
| 10-31 10:32 | +10 stop | BTC | DOWN | 0.49 | 0.62 | 0.95 |
