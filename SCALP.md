# Range-Scalp Bot

*Updated Thu Nov 05 04:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48018 | 41818 | 6200 (73) | 4 | $-13808.83 | -4.6% |
| **+10¢** | 35869 | 28669 | 7200 (99) | 5 | $-12657.56 | -5.6% |
| **+15¢** | 30057 | 22306 | 7751 (127) | 5 | $-11564.36 | -6.1% |
| **+20¢** | 26699 | 18580 | 8119 (166) | 6 | $-10227.00 | -6.1% |
| **+10¢ (15¢ stop)** | 58539 | 58446 | 93 (56) | 0 | $-21755.94 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 04:28 | +5 | XRP | DOWN | 0.66 | 0.76 | 0.76 |
| 11-05 04:27 | +10 stop | DOGE | DOWN | 0.62 | 0.87 | 2.25 |
| 11-05 04:27 | +20 | DOGE | DOWN | 0.60 | 0.87 | 2.45 |
| 11-05 04:27 | +15 | DOGE | DOWN | 0.57 | 0.87 | 2.74 |
| 11-05 04:27 | +10 | DOGE | DOWN | 0.57 | 0.69 | 0.87 |
| 11-05 04:27 | +5 | DOGE | DOWN | 0.57 | 0.69 | 0.87 |
| 11-05 04:27 | +10 stop | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 11-05 04:27 | +20 | XRP | DOWN | 0.58 | open |  |
| 11-05 04:27 | +15 | XRP | DOWN | 0.58 | 0.76 | 1.49 |
| 11-05 04:27 | +10 | XRP | DOWN | 0.59 | 0.76 | 1.40 |
| 11-05 04:27 | +5 | XRP | DOWN | 0.58 | 0.67 | 0.53 |
| 11-05 04:27 | +10 stop | SOL | DOWN | 0.66 | 0.36 | -3.33 |
| 11-05 04:27 | +10 | SOL | DOWN | 0.66 | open |  |
| 11-05 04:27 | +5 | SOL | DOWN | 0.66 | open |  |
| 11-05 04:27 | +10 stop | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 11-05 04:26 | +10 stop | ETH | UP | 0.58 | 0.69 | 0.77 |
| 11-05 04:26 | +10 stop | BTC | DOWN | 0.68 | 0.29 | -4.21 |
| 11-05 04:24 | +10 stop | BNB | UP | 0.61 | 0.92 | 2.84 |
| 11-05 04:23 | +10 stop | NEAR | DOWN | 0.70 | 0.43 | -3.03 |
| 11-05 04:23 | +10 stop | ZEC | DOWN | 0.63 | 0.76 | 1.00 |
| 11-05 04:22 | +10 stop | ETH | DOWN | 0.70 | 0.53 | -2.03 |
| 11-05 04:22 | +10 stop | BNB | UP | 0.57 | 0.42 | -1.86 |
| 11-05 04:22 | +10 stop | NEAR | UP | 0.43 | 0.54 | 0.74 |
| 11-05 04:21 | +10 stop | BTC | DOWN | 0.60 | 0.72 | 0.88 |
| 11-05 04:21 | +5 | DOGE | DOWN | 0.70 | 0.77 | 0.42 |
| 11-05 04:21 | +5 | ETH | DOWN | 0.70 | open |  |
| 11-05 04:20 | +10 stop | NEAR | DOWN | 0.63 | 0.40 | -2.64 |
| 11-05 04:20 | +10 stop | SOL | DOWN | 0.69 | 0.53 | -1.93 |
| 11-05 04:20 | +20 | SOL | DOWN | 0.69 | open |  |
| 11-05 04:20 | +10 stop | ZEC | DOWN | 0.69 | 0.48 | -2.43 |
| 11-05 04:20 | +15 | ZEC | DOWN | 0.69 | 0.87 | 1.57 |
| 11-05 04:20 | +10 | ZEC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-05 04:20 | +5 | ZEC | DOWN | 0.69 | 0.76 | 0.42 |
| 11-05 04:20 | +10 | BNB | DOWN | 0.64 | open |  |
| 11-05 04:20 | +5 | BNB | DOWN | 0.64 | open |  |
| 11-05 04:19 | +10 stop | BNB | DOWN | 0.62 | 0.40 | -2.54 |
| 11-05 04:19 | +10 stop | NEAR | DOWN | 0.48 | 0.63 | 1.15 |
| 11-05 04:19 | +15 | SOL | DOWN | 0.71 | open |  |
| 11-05 04:19 | +10 | SOL | DOWN | 0.71 | 0.83 | 0.95 |
| 11-05 04:19 | +5 | SOL | DOWN | 0.71 | 0.76 | 0.22 |
