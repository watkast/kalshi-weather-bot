# Range-Scalp Bot

*Updated Sun Nov 01 09:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43441 | 37857 | 5584 (63) | 3 | $-12389.84 | -4.5% |
| **+10¢** | 32410 | 25962 | 6448 (85) | 3 | $-11082.00 | -5.4% |
| **+15¢** | 27127 | 20183 | 6944 (112) | 3 | $-10104.84 | -5.9% |
| **+20¢** | 24092 | 16819 | 7273 (146) | 3 | $-8900.34 | -5.9% |
| **+10¢ (15¢ stop)** | 52993 | 52908 | 85 (50) | 2 | $-20023.98 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 09:55 | +10 stop | HYPE | DOWN | 0.56 | open |  |
| 11-01 09:55 | +10 stop | SOL | DOWN | 0.52 | open |  |
| 11-01 09:54 | +10 stop | SOL | UP | 0.59 | 0.44 | -1.85 |
| 11-01 09:54 | +15 | SOL | UP | 0.63 | open |  |
| 11-01 09:54 | +10 | SOL | UP | 0.64 | open |  |
| 11-01 09:54 | +5 | SOL | UP | 0.64 | open |  |
| 11-01 09:51 | +10 stop | HYPE | DOWN | 0.60 | 0.75 | 1.19 |
| 11-01 09:51 | +10 stop | SOL | UP | 0.64 | 0.80 | 1.31 |
| 11-01 09:51 | +20 | SOL | UP | 0.64 | open |  |
| 11-01 09:51 | +15 | SOL | UP | 0.64 | 0.80 | 1.31 |
| 11-01 09:51 | +10 | SOL | UP | 0.64 | 0.80 | 1.31 |
| 11-01 09:51 | +5 | SOL | UP | 0.64 | 0.80 | 1.31 |
| 11-01 09:50 | +10 stop | ETH | DOWN | 0.68 | 0.82 | 1.13 |
| 11-01 09:48 | +10 stop | ETH | UP | 0.59 | 0.44 | -1.85 |
| 11-01 09:48 | +20 | ETH | UP | 0.59 | open |  |
| 11-01 09:48 | +15 | ETH | UP | 0.59 | open |  |
| 11-01 09:48 | +10 | ETH | UP | 0.59 | open |  |
| 11-01 09:47 | +5 | ETH | UP | 0.71 | open |  |
| 11-01 09:46 | +10 stop | BTC | UP | 0.65 | 0.75 | 0.70 |
| 11-01 09:46 | +20 | BTC | UP | 0.65 | 0.85 | 1.75 |
| 11-01 09:46 | +15 | BTC | UP | 0.65 | 0.82 | 1.43 |
| 11-01 09:46 | +10 | BTC | UP | 0.65 | 0.75 | 0.70 |
| 11-01 09:46 | +5 | BTC | UP | 0.65 | 0.70 | 0.19 |
| 11-01 09:46 | +10 stop | HYPE | UP | 0.65 | 0.44 | -2.45 |
| 11-01 09:46 | +20 | HYPE | UP | 0.65 | open |  |
| 11-01 09:46 | +15 | HYPE | UP | 0.65 | open |  |
| 11-01 09:46 | +10 | HYPE | UP | 0.65 | open |  |
| 11-01 09:46 | +5 | HYPE | UP | 0.65 | open |  |
| 11-01 09:46 | +10 stop | NEAR | UP | 0.71 | 0.84 | 1.05 |
| 11-01 09:46 | +20 | NEAR | UP | 0.71 | 0.93 | 1.95 |
| 11-01 09:46 | +15 | NEAR | UP | 0.71 | 0.93 | 1.95 |
| 11-01 09:46 | +10 | NEAR | UP | 0.70 | 0.84 | 1.15 |
| 11-01 09:46 | +5 | NEAR | UP | 0.70 | 0.79 | 0.63 |
| 11-01 09:46 | +10 stop | SOL | UP | 0.64 | 0.74 | 0.69 |
| 11-01 09:46 | +20 | SOL | UP | 0.64 | 0.86 | 1.94 |
| 11-01 09:46 | +15 | SOL | UP | 0.64 | 0.80 | 1.31 |
| 11-01 09:46 | +10 | SOL | UP | 0.64 | 0.74 | 0.69 |
| 11-01 09:46 | +5 | SOL | UP | 0.64 | 0.72 | 0.48 |
| 11-01 09:45 | +10 stop | BNB | UP | 0.61 | 0.72 | 0.78 |
| 11-01 09:45 | +20 | BNB | UP | 0.61 | 0.82 | 1.82 |
