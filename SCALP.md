# Range-Scalp Bot

*Updated Tue Nov 03 03:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45538 | 39651 | 5887 (69) | 1 | $-13143.83 | -4.6% |
| **+10¢** | 33994 | 27171 | 6823 (91) | 1 | $-12039.48 | -5.6% |
| **+15¢** | 28442 | 21101 | 7341 (119) | 2 | $-11048.42 | -6.2% |
| **+20¢** | 25259 | 17567 | 7692 (154) | 2 | $-9835.71 | -6.2% |
| **+10¢ (15¢ stop)** | 55565 | 55476 | 89 (53) | 0 | $-20944.61 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 03:40 | +5 | DOGE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-03 03:39 | +10 stop | DOGE | DOWN | 0.53 | 0.66 | 0.96 |
| 11-03 03:39 | +20 | DOGE | DOWN | 0.53 | 0.78 | 2.19 |
| 11-03 03:39 | +15 | DOGE | DOWN | 0.53 | 0.71 | 1.47 |
| 11-03 03:39 | +10 | DOGE | DOWN | 0.53 | 0.66 | 0.96 |
| 11-03 03:39 | +5 | DOGE | DOWN | 0.53 | 0.58 | 0.14 |
| 11-03 03:38 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 11-03 03:38 | +20 | XRP | DOWN | 0.64 | open |  |
| 11-03 03:38 | +15 | XRP | DOWN | 0.64 | open |  |
| 11-03 03:38 | +10 | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-03 03:38 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 11-03 03:36 | +10 stop | NEAR | UP | 0.69 | 0.79 | 0.73 |
| 11-03 03:36 | +20 | NEAR | UP | 0.69 | 0.93 | 2.16 |
| 11-03 03:36 | +15 | NEAR | UP | 0.69 | 0.86 | 1.46 |
| 11-03 03:36 | +10 | NEAR | UP | 0.71 | 0.86 | 1.26 |
| 11-03 03:36 | +5 | NEAR | UP | 0.71 | 0.77 | 0.32 |
| 11-03 03:36 | +10 stop | ZEC | DOWN | 0.54 | 0.33 | -2.44 |
| 11-03 03:36 | +20 | ZEC | DOWN | 0.54 | open |  |
| 11-03 03:36 | +15 | ZEC | DOWN | 0.54 | open |  |
| 11-03 03:36 | +10 | ZEC | DOWN | 0.54 | open |  |
| 11-03 03:36 | +5 | ZEC | DOWN | 0.53 | open |  |
| 11-03 03:35 | +10 stop | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 11-03 03:35 | +10 | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 11-03 03:35 | +5 | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 11-03 03:35 | +5 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 11-03 03:34 | +10 stop | BTC | DOWN | 0.59 | 0.73 | 1.09 |
| 11-03 03:34 | +10 stop | ETH | DOWN | 0.62 | 0.77 | 1.20 |
| 11-03 03:34 | +10 stop | DOGE | DOWN | 0.54 | 0.74 | 1.68 |
| 11-03 03:32 | +10 stop | DOGE | UP | 0.63 | 0.43 | -2.35 |
| 11-03 03:32 | +10 stop | BTC | UP | 0.56 | 0.37 | -2.25 |
| 11-03 03:32 | +10 stop | ETH | UP | 0.60 | 0.37 | -2.64 |
| 11-03 03:32 | +5 | ZEC | UP | 0.68 | 0.74 | 0.30 |
| 11-03 03:31 | +10 stop | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 11-03 03:31 | +20 | XRP | DOWN | 0.67 | 0.89 | 1.97 |
| 11-03 03:31 | +15 | XRP | DOWN | 0.67 | 0.84 | 1.44 |
| 11-03 03:31 | +10 | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 11-03 03:31 | +5 | XRP | DOWN | 0.65 | 0.71 | 0.29 |
| 11-03 03:31 | +10 stop | BTC | DOWN | 0.65 | 0.49 | -1.94 |
| 11-03 03:31 | +20 | BTC | DOWN | 0.65 | 0.86 | 1.85 |
| 11-03 03:31 | +15 | BTC | DOWN | 0.65 | 0.83 | 1.54 |
