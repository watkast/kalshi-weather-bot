# Range-Scalp Bot

*Updated Sat Nov 21 05:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67106 | 58568 | 8538 (129) | 0 | $-18024.73 | -4.3% |
| **+10¢** | 50119 | 40139 | 9980 (171) | 0 | $-16751.91 | -5.3% |
| **+15¢** | 42028 | 31271 | 10757 (219) | 1 | $-15018.41 | -5.7% |
| **+20¢** | 37406 | 26103 | 11303 (276) | 2 | $-13346.47 | -5.7% |
| **+10¢ (15¢ stop)** | 81705 | 81539 | 166 (100) | 0 | $-30070.59 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 05:34 | +10 stop | NEAR | DOWN | 0.67 | 0.78 | 0.81 |
| 11-21 05:34 | +20 | NEAR | DOWN | 0.68 | open |  |
| 11-21 05:34 | +15 | NEAR | DOWN | 0.68 | open |  |
| 11-21 05:34 | +10 | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 11-21 05:34 | +5 | NEAR | DOWN | 0.69 | 0.78 | 0.62 |
| 11-21 05:33 | +10 stop | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-21 05:33 | +20 | HYPE | DOWN | 0.67 | open |  |
| 11-21 05:33 | +15 | HYPE | DOWN | 0.69 | 0.84 | 1.29 |
| 11-21 05:33 | +10 | HYPE | DOWN | 0.66 | 0.77 | 0.81 |
| 11-21 05:33 | +5 | HYPE | DOWN | 0.69 | 0.77 | 0.56 |
| 11-21 05:31 | +10 stop | ZEC | DOWN | 0.70 | 0.88 | 1.57 |
| 11-21 05:31 | +20 | ZEC | DOWN | 0.70 | 0.90 | 1.80 |
| 11-21 05:31 | +15 | ZEC | DOWN | 0.70 | 0.88 | 1.58 |
| 11-21 05:31 | +10 | ZEC | DOWN | 0.70 | 0.88 | 1.57 |
| 11-21 05:31 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-21 05:28 | +10 | SOL | UP | 0.71 | 0.93 | 2.02 |
| 11-21 05:27 | +10 stop | SOL | UP | 0.56 | 0.76 | 1.69 |
| 11-21 05:27 | +5 | SOL | UP | 0.56 | 0.61 | 0.15 |
| 11-21 05:25 | +10 stop | ETH | UP | 0.70 | 0.82 | 0.94 |
| 11-21 05:24 | +10 stop | ZEC | UP | 0.60 | 0.71 | 0.78 |
| 11-21 05:24 | +5 | ZEC | UP | 0.61 | 0.68 | 0.37 |
| 11-21 05:24 | +10 stop | DOGE | UP | 0.64 | 0.75 | 0.79 |
| 11-21 05:24 | +5 | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 11-21 05:23 | +10 stop | ETH | UP | 0.70 | 0.54 | -1.93 |
| 11-21 05:23 | +5 | ETH | UP | 0.69 | 0.74 | 0.21 |
| 11-21 05:23 | +10 stop | SOL | UP | 0.57 | 0.67 | 0.66 |
| 11-21 05:22 | +10 stop | NEAR | UP | 0.59 | 0.71 | 0.88 |
| 11-21 05:21 | +5 | ETH | UP | 0.61 | 0.69 | 0.48 |
| 11-21 05:21 | +10 stop | HYPE | UP | 0.69 | 0.80 | 0.85 |
| 11-21 05:20 | +10 stop | ZEC | UP | 0.62 | 0.72 | 0.68 |
| 11-21 05:20 | +10 stop | SOL | DOWN | 0.68 | 0.53 | -1.84 |
| 11-21 05:20 | +10 stop | XRP | UP | 0.61 | 0.73 | 0.89 |
| 11-21 05:20 | +5 | XRP | UP | 0.62 | 0.68 | 0.27 |
| 11-21 05:20 | +10 stop | DOGE | DOWN | 0.57 | 0.37 | -2.35 |
| 11-21 05:20 | +10 stop | BTC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-21 05:20 | +10 stop | ETH | DOWN | 0.52 | 0.35 | -2.04 |
| 11-21 05:20 | +5 | ETH | DOWN | 0.50 | 0.61 | 0.75 |
| 11-21 05:20 | +10 stop | BNB | UP | 0.57 | 0.68 | 0.76 |
| 11-21 05:20 | +10 | BNB | UP | 0.58 | 0.68 | 0.66 |
| 11-21 05:20 | +5 | BNB | UP | 0.58 | 0.68 | 0.66 |
