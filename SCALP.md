# Range-Scalp Bot

*Updated Thu Nov 26 21:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72947 | 63672 | 9275 (158) | 0 | $-19417.97 | -4.2% |
| **+10¢** | 54377 | 43547 | 10830 (203) | 1 | $-18021.87 | -5.3% |
| **+15¢** | 45535 | 33868 | 11667 (261) | 2 | $-16120.91 | -5.6% |
| **+20¢** | 40520 | 28237 | 12283 (327) | 4 | $-14507.49 | -5.7% |
| **+10¢ (15¢ stop)** | 88827 | 88618 | 209 (128) | 1 | $-32771.71 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 21:31 | +10 stop | NEAR | UP | 0.67 | open |  |
| 11-26 21:31 | +20 | NEAR | UP | 0.67 | open |  |
| 11-26 21:31 | +15 | NEAR | UP | 0.67 | open |  |
| 11-26 21:31 | +10 | NEAR | UP | 0.67 | open |  |
| 11-26 21:31 | +5 | NEAR | UP | 0.68 | 0.73 | 0.20 |
| 11-26 21:31 | +10 stop | ETH | UP | 0.68 | 0.84 | 1.34 |
| 11-26 21:31 | +20 | ETH | UP | 0.68 | 0.89 | 1.87 |
| 11-26 21:31 | +15 | ETH | UP | 0.68 | 0.84 | 1.34 |
| 11-26 21:31 | +10 | ETH | UP | 0.68 | 0.84 | 1.34 |
| 11-26 21:31 | +5 | ETH | UP | 0.68 | 0.73 | 0.20 |
| 11-26 21:31 | +10 stop | HYPE | UP | 0.62 | 0.72 | 0.68 |
| 11-26 21:31 | +20 | HYPE | UP | 0.62 | open |  |
| 11-26 21:31 | +15 | HYPE | UP | 0.62 | open |  |
| 11-26 21:31 | +10 | HYPE | UP | 0.62 | 0.72 | 0.68 |
| 11-26 21:31 | +5 | HYPE | UP | 0.62 | 0.72 | 0.68 |
| 11-26 21:31 | +10 stop | BTC | UP | 0.68 | 0.78 | 0.71 |
| 11-26 21:31 | +20 | BTC | UP | 0.68 | open |  |
| 11-26 21:31 | +15 | BTC | UP | 0.68 | 0.83 | 1.24 |
| 11-26 21:31 | +10 | BTC | UP | 0.68 | 0.78 | 0.71 |
| 11-26 21:31 | +5 | BTC | UP | 0.68 | 0.75 | 0.40 |
| 11-26 21:31 | +10 stop | DOGE | UP | 0.71 | 0.84 | 1.05 |
| 11-26 21:31 | +20 | DOGE | UP | 0.71 | open |  |
| 11-26 21:31 | +15 | DOGE | UP | 0.71 | 0.87 | 1.37 |
| 11-26 21:31 | +10 | DOGE | UP | 0.71 | 0.84 | 1.05 |
| 11-26 21:31 | +5 | DOGE | UP | 0.71 | 0.84 | 1.05 |
| 11-26 21:31 | +10 stop | SOL | UP | 0.68 | 0.87 | 1.66 |
| 11-26 21:31 | +20 | SOL | UP | 0.68 | 0.88 | 1.76 |
| 11-26 21:31 | +15 | SOL | UP | 0.68 | 0.87 | 1.66 |
| 11-26 21:31 | +10 | SOL | UP | 0.68 | 0.87 | 1.66 |
| 11-26 21:31 | +5 | SOL | UP | 0.68 | 0.76 | 0.51 |
| 11-26 21:28 | +10 stop | ETH | UP | 0.60 | 0.82 | 1.92 |
| 11-26 21:28 | +10 | ETH | UP | 0.60 | 0.82 | 1.92 |
| 11-26 21:28 | +5 | ETH | UP | 0.61 | 0.82 | 1.82 |
| 11-26 21:27 | +5 | HYPE | DOWN | 0.71 | 0.88 | 1.47 |
| 11-26 21:27 | +10 stop | DOGE | UP | 0.53 | 0.15 | -4.07 |
| 11-26 21:27 | +10 | DOGE | UP | 0.53 | no | -5.48 |
| 11-26 21:27 | +5 | DOGE | UP | 0.53 | 0.60 | 0.35 |
| 11-26 21:27 | +10 stop | NEAR | UP | 0.49 | 0.61 | 0.85 |
| 11-26 21:27 | +10 | NEAR | UP | 0.48 | 0.61 | 0.95 |
| 11-26 21:27 | +5 | NEAR | UP | 0.48 | 0.61 | 0.95 |
