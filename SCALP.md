# Range-Scalp Bot

*Updated Tue Nov 17 17:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63116 | 55061 | 8055 (117) | 1 | $-17144.84 | -4.3% |
| **+10¢** | 47153 | 37730 | 9423 (159) | 1 | $-15991.54 | -5.4% |
| **+15¢** | 39527 | 29366 | 10161 (201) | 1 | $-14494.28 | -5.8% |
| **+20¢** | 35217 | 24555 | 10662 (256) | 2 | $-12726.14 | -5.8% |
| **+10¢ (15¢ stop)** | 76797 | 76641 | 156 (92) | 0 | $-28276.39 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 17:58 | +10 stop | DOGE | DOWN | 0.70 | 0.55 | -1.83 |
| 11-17 17:58 | +20 | DOGE | DOWN | 0.70 | 0.90 | 1.80 |
| 11-17 17:58 | +15 | DOGE | DOWN | 0.70 | 0.90 | 1.77 |
| 11-17 17:58 | +10 | DOGE | DOWN | 0.70 | 0.90 | 1.77 |
| 11-17 17:58 | +5 | DOGE | DOWN | 0.70 | 0.90 | 1.77 |
| 11-17 17:56 | +10 stop | SOL | UP | 0.62 | 0.72 | 0.68 |
| 11-17 17:56 | +20 | SOL | UP | 0.62 | 0.83 | 1.83 |
| 11-17 17:56 | +15 | SOL | UP | 0.62 | 0.83 | 1.83 |
| 11-17 17:56 | +10 | SOL | UP | 0.62 | 0.72 | 0.68 |
| 11-17 17:56 | +5 | SOL | UP | 0.62 | 0.72 | 0.68 |
| 11-17 17:56 | +10 stop | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 11-17 17:56 | +20 | XRP | DOWN | 0.62 | 0.88 | 2.35 |
| 11-17 17:56 | +15 | XRP | DOWN | 0.62 | 0.81 | 1.62 |
| 11-17 17:56 | +10 | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 11-17 17:56 | +5 | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 11-17 17:56 | +10 stop | ZEC | UP | 0.55 | 0.66 | 0.77 |
| 11-17 17:56 | +20 | ZEC | UP | 0.55 | 0.76 | 1.80 |
| 11-17 17:56 | +15 | ZEC | UP | 0.55 | 0.76 | 1.80 |
| 11-17 17:56 | +10 | ZEC | UP | 0.55 | 0.66 | 0.77 |
| 11-17 17:56 | +5 | ZEC | UP | 0.55 | 0.62 | 0.36 |
| 11-17 17:53 | +10 stop | HYPE | UP | 0.61 | 0.76 | 1.20 |
| 11-17 17:53 | +20 | HYPE | UP | 0.61 | open |  |
| 11-17 17:53 | +15 | HYPE | UP | 0.61 | 0.76 | 1.20 |
| 11-17 17:53 | +10 | HYPE | UP | 0.61 | 0.76 | 1.20 |
| 11-17 17:53 | +5 | HYPE | UP | 0.61 | 0.67 | 0.27 |
| 11-17 17:51 | +10 stop | NEAR | UP | 0.69 | 0.51 | -2.16 |
| 11-17 17:51 | +20 | NEAR | UP | 0.69 | open |  |
| 11-17 17:51 | +15 | NEAR | UP | 0.69 | open |  |
| 11-17 17:51 | +10 | NEAR | UP | 0.69 | open |  |
| 11-17 17:51 | +5 | NEAR | UP | 0.69 | open |  |
| 11-17 17:49 | +5 | XRP | UP | 0.60 | 0.68 | 0.47 |
| 11-17 17:48 | +10 stop | DOGE | UP | 0.58 | 0.68 | 0.66 |
| 11-17 17:48 | +10 stop | XRP | DOWN | 0.50 | 0.31 | -2.23 |
| 11-17 17:48 | +10 stop | ETH | UP | 0.71 | 0.84 | 1.05 |
| 11-17 17:48 | +20 | ETH | UP | 0.71 | 0.91 | 1.83 |
| 11-17 17:48 | +15 | ETH | UP | 0.71 | 0.86 | 1.26 |
| 11-17 17:48 | +10 | ETH | UP | 0.71 | 0.84 | 1.05 |
| 11-17 17:48 | +5 | ETH | UP | 0.71 | 0.78 | 0.42 |
| 11-17 17:48 | +5 | XRP | DOWN | 0.49 | 0.56 | 0.34 |
| 11-17 17:47 | +10 stop | BNB | UP | 0.66 | 0.82 | 1.32 |
