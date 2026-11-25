# Range-Scalp Bot

*Updated Wed Nov 25 15:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71681 | 62558 | 9123 (158) | 2 | $-19144.51 | -4.2% |
| **+10¢** | 53466 | 42813 | 10653 (203) | 3 | $-17750.44 | -5.3% |
| **+15¢** | 44779 | 33309 | 11470 (260) | 5 | $-15802.88 | -5.6% |
| **+20¢** | 39870 | 27791 | 12079 (326) | 6 | $-14200.83 | -5.7% |
| **+10¢ (15¢ stop)** | 87284 | 87075 | 209 (128) | 2 | $-32075.37 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 15:21 | +5 | SOL | DOWN | 0.51 | 0.61 | 0.65 |
| 11-25 15:21 | +10 stop | ZEC | DOWN | 0.59 | open |  |
| 11-25 15:21 | +15 | ZEC | DOWN | 0.59 | open |  |
| 11-25 15:21 | +10 | ZEC | DOWN | 0.59 | open |  |
| 11-25 15:21 | +5 | ZEC | DOWN | 0.59 | open |  |
| 11-25 15:20 | +5 | ETH | DOWN | 0.71 | open |  |
| 11-25 15:19 | +10 stop | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 11-25 15:19 | +20 | ETH | DOWN | 0.71 | open |  |
| 11-25 15:19 | +15 | ETH | DOWN | 0.71 | open |  |
| 11-25 15:19 | +10 | ETH | DOWN | 0.71 | open |  |
| 11-25 15:19 | +5 | ETH | DOWN | 0.71 | 0.80 | 0.63 |
| 11-25 15:18 | +10 stop | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-25 15:18 | +20 | ZEC | DOWN | 0.67 | open |  |
| 11-25 15:18 | +15 | ZEC | DOWN | 0.67 | 0.83 | 1.34 |
| 11-25 15:18 | +10 | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-25 15:18 | +5 | ZEC | DOWN | 0.67 | 0.76 | 0.61 |
| 11-25 15:17 | +10 stop | DOGE | DOWN | 0.67 | 0.51 | -1.94 |
| 11-25 15:17 | +20 | DOGE | DOWN | 0.66 | open |  |
| 11-25 15:17 | +15 | DOGE | DOWN | 0.66 | open |  |
| 11-25 15:17 | +10 | DOGE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-25 15:17 | +5 | DOGE | DOWN | 0.67 | 0.73 | 0.30 |
| 11-25 15:16 | +10 stop | SOL | DOWN | 0.71 | open |  |
| 11-25 15:16 | +20 | SOL | DOWN | 0.71 | open |  |
| 11-25 15:16 | +15 | SOL | DOWN | 0.71 | open |  |
| 11-25 15:16 | +10 | SOL | DOWN | 0.71 | open |  |
| 11-25 15:16 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.42 |
| 11-25 15:16 | +10 stop | NEAR | DOWN | 0.71 | 0.83 | 0.95 |
| 11-25 15:16 | +20 | NEAR | DOWN | 0.71 | open |  |
| 11-25 15:16 | +15 | NEAR | DOWN | 0.71 | 0.87 | 1.37 |
| 11-25 15:16 | +10 | NEAR | DOWN | 0.71 | 0.83 | 0.95 |
| 11-25 15:16 | +5 | NEAR | DOWN | 0.71 | 0.77 | 0.32 |
| 11-25 15:16 | +10 stop | XRP | DOWN | 0.69 | 0.53 | -1.93 |
| 11-25 15:16 | +20 | XRP | DOWN | 0.70 | open |  |
| 11-25 15:16 | +15 | XRP | DOWN | 0.68 | open |  |
| 11-25 15:16 | +10 | XRP | DOWN | 0.68 | 0.81 | 1.03 |
| 11-25 15:16 | +5 | XRP | DOWN | 0.68 | 0.77 | 0.61 |
| 11-25 15:15 | +10 stop | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-25 15:15 | +20 | BTC | DOWN | 0.61 | 0.81 | 1.72 |
| 11-25 15:15 | +15 | BTC | DOWN | 0.59 | 0.76 | 1.40 |
| 11-25 15:15 | +10 | BTC | DOWN | 0.60 | 0.76 | 1.30 |
