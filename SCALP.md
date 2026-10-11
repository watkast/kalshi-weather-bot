# Range-Scalp Bot

*Updated Sun Oct 11 16:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12204 | 10527 | 1677 (24) | 4 | $-4076.69 | -5.3% |
| **+10¢** | 9270 | 7325 | 1945 (37) | 5 | $-3844.95 | -6.6% |
| **+15¢** | 7812 | 5746 | 2066 (54) | 5 | $-3295.31 | -6.7% |
| **+20¢** | 6960 | 4807 | 2153 (68) | 5 | $-2801.03 | -6.4% |
| **+10¢ (15¢ stop)** | 15036 | 14995 | 41 (25) | 1 | $-5930.63 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 16:53 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 10-11 16:53 | +10 stop | BTC | UP | 0.65 | 0.80 | 1.22 |
| 10-11 16:53 | +10 stop | SOL | UP | 0.60 | 0.72 | 0.88 |
| 10-11 16:53 | +5 | XRP | DOWN | 0.61 | 0.66 | 0.17 |
| 10-11 16:51 | +10 | XRP | DOWN | 0.60 | open |  |
| 10-11 16:51 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 10-11 16:51 | +10 stop | DOGE | DOWN | 0.53 | open |  |
| 10-11 16:51 | +5 | SOL | DOWN | 0.58 | open |  |
| 10-11 16:50 | +10 stop | SOL | DOWN | 0.58 | 0.43 | -1.86 |
| 10-11 16:50 | +10 stop | ZEC | UP | 0.59 | 0.33 | -2.93 |
| 10-11 16:50 | +10 | ZEC | UP | 0.59 | open |  |
| 10-11 16:50 | +5 | ZEC | UP | 0.59 | open |  |
| 10-11 16:50 | +10 stop | XRP | DOWN | 0.71 | 0.45 | -2.93 |
| 10-11 16:50 | +5 | NEAR | UP | 0.58 | 0.67 | 0.56 |
| 10-11 16:49 | +10 stop | BNB | DOWN | 0.68 | 0.81 | 1.05 |
| 10-11 16:49 | +15 | BNB | DOWN | 0.68 | 0.83 | 1.26 |
| 10-11 16:49 | +10 | BNB | DOWN | 0.68 | 0.81 | 1.04 |
| 10-11 16:49 | +5 | BNB | DOWN | 0.68 | 0.76 | 0.52 |
| 10-11 16:49 | +10 stop | SOL | UP | 0.53 | 0.66 | 0.96 |
| 10-11 16:49 | +10 stop | DOGE | UP | 0.64 | 0.48 | -1.95 |
| 10-11 16:49 | +10 stop | BTC | UP | 0.51 | 0.68 | 1.36 |
| 10-11 16:48 | +10 stop | ZEC | DOWN | 0.38 | 0.53 | 1.15 |
| 10-11 16:48 | +5 | NEAR | UP | 0.55 | 0.62 | 0.35 |
| 10-11 16:48 | +10 stop | ETH | UP | 0.57 | 0.73 | 1.28 |
| 10-11 16:48 | +20 | ETH | UP | 0.57 | 0.77 | 1.69 |
| 10-11 16:48 | +15 | ETH | UP | 0.57 | 0.73 | 1.28 |
| 10-11 16:48 | +10 | ETH | UP | 0.57 | 0.73 | 1.28 |
| 10-11 16:48 | +5 | ETH | UP | 0.57 | 0.62 | 0.15 |
| 10-11 16:47 | +10 stop | XRP | DOWN | 0.63 | 0.46 | -2.05 |
| 10-11 16:47 | +20 | XRP | DOWN | 0.63 | open |  |
| 10-11 16:47 | +15 | XRP | DOWN | 0.63 | open |  |
| 10-11 16:47 | +10 | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-11 16:47 | +5 | XRP | DOWN | 0.64 | 0.69 | 0.18 |
| 10-11 16:47 | +5 | BNB | DOWN | 0.52 | 0.70 | 1.47 |
| 10-11 16:47 | +10 stop | SOL | DOWN | 0.50 | 0.28 | -2.53 |
| 10-11 16:47 | +20 | SOL | DOWN | 0.50 | open |  |
| 10-11 16:47 | +15 | SOL | DOWN | 0.50 | open |  |
| 10-11 16:47 | +10 | SOL | DOWN | 0.50 | open |  |
| 10-11 16:47 | +5 | SOL | DOWN | 0.50 | 0.55 | 0.14 |
| 10-11 16:46 | +10 stop | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
