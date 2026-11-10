# Range-Scalp Bot

*Updated Tue Nov 10 22:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54993 | 47960 | 7033 (94) | 4 | $-15025.84 | -4.3% |
| **+10¢** | 41094 | 32892 | 8202 (124) | 4 | $-13925.08 | -5.4% |
| **+15¢** | 34451 | 25614 | 8837 (158) | 4 | $-12638.03 | -5.8% |
| **+20¢** | 30667 | 21395 | 9272 (207) | 4 | $-11062.66 | -5.8% |
| **+10¢ (15¢ stop)** | 67006 | 66888 | 118 (73) | 0 | $-24770.62 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 22:43 | +10 stop | NEAR | DOWN | 0.69 | 0.33 | -3.91 |
| 11-10 22:43 | +20 | NEAR | DOWN | 0.69 | open |  |
| 11-10 22:43 | +15 | NEAR | DOWN | 0.69 | open |  |
| 11-10 22:43 | +10 | NEAR | DOWN | 0.69 | open |  |
| 11-10 22:43 | +5 | NEAR | DOWN | 0.69 | open |  |
| 11-10 22:41 | +10 stop | ETH | DOWN | 0.70 | 0.84 | 1.15 |
| 11-10 22:41 | +10 stop | ZEC | DOWN | 0.41 | 0.58 | 1.35 |
| 11-10 22:41 | +10 | ZEC | DOWN | 0.42 | 0.58 | 1.24 |
| 11-10 22:41 | +5 | ZEC | DOWN | 0.42 | 0.58 | 1.24 |
| 11-10 22:40 | +10 stop | DOGE | UP | 0.53 | 0.75 | 1.88 |
| 11-10 22:39 | +10 stop | ETH | DOWN | 0.71 | 0.46 | -2.83 |
| 11-10 22:39 | +20 | ETH | DOWN | 0.71 | 0.97 | 2.41 |
| 11-10 22:39 | +15 | ETH | DOWN | 0.71 | 0.90 | 1.70 |
| 11-10 22:39 | +10 | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 11-10 22:39 | +5 | ETH | DOWN | 0.71 | 0.78 | 0.42 |
| 11-10 22:38 | +10 stop | NEAR | DOWN | 0.54 | 0.35 | -2.24 |
| 11-10 22:38 | +20 | NEAR | DOWN | 0.54 | 0.79 | 2.20 |
| 11-10 22:38 | +10 | NEAR | DOWN | 0.54 | 0.72 | 1.47 |
| 11-10 22:38 | +5 | NEAR | DOWN | 0.54 | 0.60 | 0.25 |
| 11-10 22:38 | +10 stop | ZEC | UP | 0.64 | 0.74 | 0.69 |
| 11-10 22:37 | +10 stop | BNB | UP | 0.46 | 0.62 | 1.25 |
| 11-10 22:36 | +10 stop | BTC | UP | 0.59 | 0.71 | 0.88 |
| 11-10 22:36 | +10 stop | BNB | UP | 0.46 | 0.57 | 0.74 |
| 11-10 22:36 | +15 | DOGE | DOWN | 0.69 | open |  |
| 11-10 22:36 | +5 | DOGE | DOWN | 0.69 | open |  |
| 11-10 22:34 | +10 stop | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 11-10 22:34 | +15 | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 11-10 22:34 | +10 | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 11-10 22:34 | +5 | BNB | DOWN | 0.63 | open |  |
| 11-10 22:34 | +5 | NEAR | DOWN | 0.69 | 0.76 | 0.42 |
| 11-10 22:33 | +10 stop | ZEC | DOWN | 0.57 | 0.42 | -1.86 |
| 11-10 22:33 | +10 stop | DOGE | DOWN | 0.66 | 0.36 | -3.33 |
| 11-10 22:33 | +10 | DOGE | DOWN | 0.66 | open |  |
| 11-10 22:33 | +5 | DOGE | DOWN | 0.66 | 0.73 | 0.40 |
| 11-10 22:32 | +10 stop | BTC | DOWN | 0.61 | 0.35 | -2.93 |
| 11-10 22:32 | +20 | BTC | DOWN | 0.61 | open |  |
| 11-10 22:32 | +15 | BTC | DOWN | 0.60 | open |  |
| 11-10 22:32 | +10 | BTC | DOWN | 0.59 | open |  |
| 11-10 22:32 | +5 | BTC | DOWN | 0.58 | open |  |
| 11-10 22:32 | +10 stop | BNB | DOWN | 0.59 | 0.43 | -1.95 |
