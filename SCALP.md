# Range-Scalp Bot

*Updated Thu Oct 15 16:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17783 | 15429 | 2354 (28) | 2 | $-5506.36 | -4.9% |
| **+10¢** | 13432 | 10708 | 2724 (40) | 4 | $-4995.62 | -5.9% |
| **+15¢** | 11266 | 8339 | 2927 (59) | 5 | $-4486.25 | -6.3% |
| **+20¢** | 10016 | 6953 | 3063 (77) | 5 | $-3918.66 | -6.2% |
| **+10¢ (15¢ stop)** | 21905 | 21855 | 50 (29) | 0 | $-8465.81 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 16:13 | +10 stop | BTC | DOWN | 0.29 | 0.64 | 3.18 |
| 10-15 16:12 | +10 stop | ETH | UP | 0.49 | 0.74 | 2.18 |
| 10-15 16:12 | +10 stop | ZEC | UP | 0.66 | 0.93 | 2.44 |
| 10-15 16:11 | +10 stop | BTC | UP | 0.70 | 0.47 | -2.63 |
| 10-15 16:11 | +5 | BTC | UP | 0.67 | 0.72 | 0.19 |
| 10-15 16:11 | +10 stop | SOL | DOWN | 0.59 | 0.76 | 1.40 |
| 10-15 16:11 | +10 stop | XRP | DOWN | 0.52 | 0.78 | 2.29 |
| 10-15 16:11 | +5 | XRP | DOWN | 0.52 | 0.59 | 0.35 |
| 10-15 16:10 | +10 stop | ETH | UP | 0.67 | 0.83 | 1.34 |
| 10-15 16:10 | +10 stop | BTC | UP | 0.68 | 0.79 | 0.82 |
| 10-15 16:10 | +5 | BTC | UP | 0.68 | 0.79 | 0.82 |
| 10-15 16:10 | +10 stop | SOL | DOWN | 0.65 | 0.46 | -2.24 |
| 10-15 16:10 | +20 | SOL | DOWN | 0.65 | 0.86 | 1.85 |
| 10-15 16:10 | +15 | SOL | DOWN | 0.65 | 0.86 | 1.85 |
| 10-15 16:10 | +10 | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 10-15 16:10 | +5 | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 10-15 16:10 | +10 stop | BNB | UP | 0.55 | 0.66 | 0.76 |
| 10-15 16:10 | +5 | XRP | UP | 0.47 | 0.64 | 1.34 |
| 10-15 16:09 | +5 | BNB | UP | 0.68 | 0.74 | 0.26 |
| 10-15 16:09 | +10 stop | HYPE | DOWN | 0.59 | 0.44 | -1.85 |
| 10-15 16:08 | +10 stop | BTC | UP | 0.54 | 0.67 | 0.96 |
| 10-15 16:08 | +5 | BTC | UP | 0.58 | 0.67 | 0.56 |
| 10-15 16:08 | +10 stop | ZEC | DOWN | 0.57 | 0.26 | -3.42 |
| 10-15 16:08 | +10 | ZEC | DOWN | 0.57 | open |  |
| 10-15 16:08 | +5 | ZEC | DOWN | 0.63 | open |  |
| 10-15 16:07 | +10 stop | ETH | UP | 0.64 | 0.78 | 1.11 |
| 10-15 16:07 | +10 stop | DOGE | DOWN | 0.58 | 0.41 | -2.06 |
| 10-15 16:07 | +20 | DOGE | DOWN | 0.58 | 0.79 | 1.79 |
| 10-15 16:07 | +15 | DOGE | DOWN | 0.58 | 0.75 | 1.37 |
| 10-15 16:07 | +10 | DOGE | DOWN | 0.58 | 0.70 | 0.86 |
| 10-15 16:07 | +5 | DOGE | DOWN | 0.58 | 0.70 | 0.86 |
| 10-15 16:06 | +10 stop | BNB | DOWN | 0.54 | 0.32 | -2.54 |
| 10-15 16:06 | +20 | BNB | DOWN | 0.54 | 0.74 | 1.68 |
| 10-15 16:06 | +15 | BNB | DOWN | 0.54 | 0.74 | 1.68 |
| 10-15 16:06 | +10 | BNB | DOWN | 0.54 | 0.74 | 1.68 |
| 10-15 16:06 | +5 | BNB | DOWN | 0.54 | 0.61 | 0.35 |
| 10-15 16:06 | +10 stop | BTC | DOWN | 0.53 | 0.37 | -1.95 |
| 10-15 16:06 | +15 | BTC | DOWN | 0.53 | open |  |
| 10-15 16:06 | +10 | BTC | DOWN | 0.53 | 0.64 | 0.75 |
| 10-15 16:06 | +5 | BTC | DOWN | 0.53 | 0.59 | 0.25 |
