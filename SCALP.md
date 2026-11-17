# Range-Scalp Bot

*Updated Tue Nov 17 19:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63209 | 55136 | 8073 (117) | 4 | $-17227.70 | -4.3% |
| **+10¢** | 47221 | 37775 | 9446 (159) | 5 | $-16092.67 | -5.4% |
| **+15¢** | 39586 | 29402 | 10184 (201) | 7 | $-14585.90 | -5.9% |
| **+20¢** | 35267 | 24579 | 10688 (256) | 7 | $-12839.49 | -5.8% |
| **+10¢ (15¢ stop)** | 76934 | 76778 | 156 (92) | 2 | $-28320.32 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 19:24 | +10 stop | SOL | DOWN | 0.63 | open |  |
| 11-17 19:23 | +10 stop | DOGE | UP | 0.57 | open |  |
| 11-17 19:23 | +15 | DOGE | UP | 0.57 | open |  |
| 11-17 19:23 | +5 | DOGE | UP | 0.57 | open |  |
| 11-17 19:22 | +10 | SOL | UP | 0.69 | open |  |
| 11-17 19:22 | +10 stop | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 11-17 19:22 | +20 | ETH | DOWN | 0.69 | open |  |
| 11-17 19:22 | +15 | ETH | DOWN | 0.69 | open |  |
| 11-17 19:22 | +10 | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 11-17 19:22 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 11-17 19:22 | +10 stop | BTC | DOWN | 0.68 | 0.82 | 1.13 |
| 11-17 19:22 | +20 | BTC | DOWN | 0.70 | open |  |
| 11-17 19:22 | +15 | BTC | DOWN | 0.70 | open |  |
| 11-17 19:22 | +10 | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-17 19:22 | +5 | BTC | DOWN | 0.71 | 0.77 | 0.32 |
| 11-17 19:22 | +10 stop | SOL | UP | 0.65 | 0.49 | -1.94 |
| 11-17 19:22 | +5 | DOGE | UP | 0.63 | 0.70 | 0.38 |
| 11-17 19:21 | +10 stop | BNB | DOWN | 0.65 | 0.79 | 1.12 |
| 11-17 19:21 | +15 | BNB | DOWN | 0.65 | 0.84 | 1.64 |
| 11-17 19:21 | +10 | BNB | DOWN | 0.66 | 0.79 | 1.02 |
| 11-17 19:21 | +5 | BNB | DOWN | 0.64 | 0.71 | 0.36 |
| 11-17 19:20 | +5 | NEAR | UP | 0.52 | open |  |
| 11-17 19:19 | +5 | SOL | DOWN | 0.59 | open |  |
| 11-17 19:19 | +10 stop | BTC | DOWN | 0.66 | 0.78 | 0.91 |
| 11-17 19:19 | +5 | BTC | DOWN | 0.66 | 0.72 | 0.29 |
| 11-17 19:19 | +10 stop | SOL | DOWN | 0.58 | 0.36 | -2.55 |
| 11-17 19:19 | +5 | ETH | DOWN | 0.68 | 0.73 | 0.20 |
| 11-17 19:19 | +10 stop | DOGE | DOWN | 0.51 | 0.29 | -2.53 |
| 11-17 19:19 | +10 stop | BNB | DOWN | 0.63 | 0.75 | 0.87 |
| 11-17 19:19 | +5 | BNB | DOWN | 0.63 | 0.69 | 0.28 |
| 11-17 19:19 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.91 |
| 11-17 19:19 | +10 stop | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 11-17 19:18 | +10 stop | NEAR | UP | 0.56 | 0.41 | -1.85 |
| 11-17 19:18 | +15 | NEAR | UP | 0.56 | open |  |
| 11-17 19:18 | +10 | NEAR | UP | 0.56 | open |  |
| 11-17 19:18 | +5 | NEAR | UP | 0.56 | 0.62 | 0.25 |
| 11-17 19:18 | +5 | DOGE | UP | 0.56 | 0.61 | 0.15 |
| 11-17 19:18 | +5 | XRP | UP | 0.60 | 0.80 | 1.71 |
| 11-17 19:18 | +10 stop | SOL | UP | 0.59 | 0.39 | -2.34 |
| 11-17 19:18 | +20 | SOL | UP | 0.58 | open |  |
