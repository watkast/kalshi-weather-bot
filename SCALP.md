# Range-Scalp Bot

*Updated Mon Nov 16 20:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62213 | 54280 | 7933 (117) | 3 | $-16811.46 | -4.3% |
| **+10¢** | 46456 | 37173 | 9283 (159) | 3 | $-15677.69 | -5.4% |
| **+15¢** | 38927 | 28912 | 10015 (200) | 3 | $-14282.47 | -5.8% |
| **+20¢** | 34701 | 24199 | 10502 (255) | 3 | $-12453.58 | -5.7% |
| **+10¢ (15¢ stop)** | 75726 | 75570 | 156 (92) | 0 | $-27941.38 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 20:34 | +5 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-16 20:32 | +10 stop | ZEC | DOWN | 0.58 | 0.72 | 1.07 |
| 11-16 20:32 | +10 stop | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 11-16 20:32 | +10 stop | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 11-16 20:32 | +20 | NEAR | DOWN | 0.63 | 0.87 | 2.15 |
| 11-16 20:32 | +15 | NEAR | DOWN | 0.63 | 0.80 | 1.41 |
| 11-16 20:32 | +10 | NEAR | DOWN | 0.64 | 0.77 | 1.00 |
| 11-16 20:32 | +5 | NEAR | DOWN | 0.64 | 0.70 | 0.28 |
| 11-16 20:32 | +10 stop | XRP | DOWN | 0.65 | 0.77 | 0.91 |
| 11-16 20:32 | +10 stop | DOGE | DOWN | 0.71 | 0.84 | 1.05 |
| 11-16 20:32 | +20 | DOGE | DOWN | 0.71 | 0.93 | 1.99 |
| 11-16 20:32 | +15 | DOGE | DOWN | 0.71 | 0.87 | 1.37 |
| 11-16 20:32 | +10 | DOGE | DOWN | 0.71 | 0.84 | 1.05 |
| 11-16 20:32 | +5 | DOGE | DOWN | 0.71 | 0.78 | 0.42 |
| 11-16 20:31 | +10 stop | BTC | DOWN | 0.68 | 0.84 | 1.34 |
| 11-16 20:31 | +20 | BTC | DOWN | 0.68 | 0.93 | 2.29 |
| 11-16 20:31 | +15 | BTC | DOWN | 0.67 | 0.84 | 1.44 |
| 11-16 20:31 | +10 | BTC | DOWN | 0.67 | 0.84 | 1.44 |
| 11-16 20:31 | +5 | BTC | DOWN | 0.67 | 0.73 | 0.30 |
| 11-16 20:31 | +10 stop | ETH | DOWN | 0.64 | 0.75 | 0.82 |
| 11-16 20:31 | +20 | ETH | DOWN | 0.64 | 0.85 | 1.87 |
| 11-16 20:31 | +15 | ETH | DOWN | 0.63 | 0.85 | 1.95 |
| 11-16 20:31 | +10 | ETH | DOWN | 0.63 | 0.75 | 0.90 |
| 11-16 20:31 | +5 | ETH | DOWN | 0.62 | 0.75 | 0.99 |
| 11-16 20:31 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.82 |
| 11-16 20:31 | +20 | HYPE | DOWN | 0.67 | 0.88 | 1.87 |
| 11-16 20:31 | +15 | HYPE | DOWN | 0.67 | 0.84 | 1.45 |
| 11-16 20:31 | +10 | HYPE | DOWN | 0.66 | 0.78 | 0.91 |
| 11-16 20:31 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-16 20:31 | +10 stop | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 11-16 20:31 | +20 | SOL | DOWN | 0.69 | 0.92 | 2.13 |
| 11-16 20:31 | +15 | SOL | DOWN | 0.67 | 0.83 | 1.34 |
| 11-16 20:31 | +10 | SOL | DOWN | 0.68 | 0.79 | 0.83 |
| 11-16 20:31 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.22 |
| 11-16 20:31 | +10 stop | ZEC | UP | 0.60 | 0.45 | -1.85 |
| 11-16 20:31 | +20 | ZEC | UP | 0.60 | open |  |
| 11-16 20:31 | +15 | ZEC | UP | 0.60 | open |  |
| 11-16 20:31 | +10 | ZEC | UP | 0.60 | open |  |
| 11-16 20:31 | +5 | ZEC | UP | 0.60 | open |  |
| 11-16 20:30 | +10 stop | XRP | UP | 0.59 | 0.41 | -2.14 |
