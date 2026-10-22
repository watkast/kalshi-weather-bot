# Range-Scalp Bot

*Updated Thu Oct 22 13:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28769 | 25071 | 3698 (39) | 4 | $-8260.68 | -4.6% |
| **+10¢** | 21592 | 17312 | 4280 (55) | 5 | $-7354.95 | -5.4% |
| **+15¢** | 18069 | 13467 | 4602 (78) | 6 | $-6575.23 | -5.8% |
| **+20¢** | 15987 | 11160 | 4827 (100) | 6 | $-5931.36 | -5.9% |
| **+10¢ (15¢ stop)** | 35281 | 35222 | 59 (32) | 4 | $-13217.96 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 13:08 | +5 | DOGE | UP | 0.55 | 0.62 | 0.35 |
| 10-22 13:08 | +10 stop | BNB | DOWN | 0.69 | open |  |
| 10-22 13:08 | +10 stop | ETH | DOWN | 0.64 | open |  |
| 10-22 13:08 | +10 | ETH | DOWN | 0.64 | open |  |
| 10-22 13:08 | +5 | ETH | DOWN | 0.64 | open |  |
| 10-22 13:07 | +10 stop | DOGE | UP | 0.62 | open |  |
| 10-22 13:07 | +10 stop | BTC | UP | 0.66 | open |  |
| 10-22 13:07 | +5 | DOGE | UP | 0.57 | 0.62 | 0.15 |
| 10-22 13:07 | +10 stop | BTC | DOWN | 0.43 | 0.55 | 0.84 |
| 10-22 13:07 | +10 stop | DOGE | DOWN | 0.59 | 0.43 | -1.95 |
| 10-22 13:07 | +5 | DOGE | DOWN | 0.59 | 0.65 | 0.27 |
| 10-22 13:06 | +10 stop | SOL | UP | 0.56 | 0.31 | -2.83 |
| 10-22 13:06 | +10 | BTC | UP | 0.67 | open |  |
| 10-22 13:06 | +5 | BTC | UP | 0.67 | open |  |
| 10-22 13:06 | +5 | SOL | UP | 0.55 | open |  |
| 10-22 13:06 | +5 | NEAR | DOWN | 0.69 | 0.83 | 1.15 |
| 10-22 13:05 | +10 stop | DOGE | UP | 0.64 | 0.37 | -3.04 |
| 10-22 13:05 | +10 stop | BTC | UP | 0.70 | 0.55 | -1.83 |
| 10-22 13:05 | +5 | SOL | DOWN | 0.58 | 0.63 | 0.15 |
| 10-22 13:05 | +10 stop | ETH | DOWN | 0.57 | 0.70 | 0.97 |
| 10-22 13:04 | +10 stop | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-22 13:04 | +10 | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-22 13:04 | +5 | HYPE | DOWN | 0.68 | 0.77 | 0.61 |
| 10-22 13:04 | +10 stop | DOGE | UP | 0.51 | 0.65 | 1.06 |
| 10-22 13:04 | +10 stop | NEAR | DOWN | 0.65 | 0.83 | 1.54 |
| 10-22 13:04 | +20 | NEAR | DOWN | 0.65 | 0.87 | 1.96 |
| 10-22 13:04 | +15 | NEAR | DOWN | 0.65 | 0.83 | 1.54 |
| 10-22 13:04 | +10 | NEAR | DOWN | 0.65 | 0.83 | 1.54 |
| 10-22 13:04 | +5 | NEAR | DOWN | 0.65 | 0.70 | 0.19 |
| 10-22 13:04 | +10 stop | SOL | DOWN | 0.61 | 0.41 | -2.34 |
| 10-22 13:04 | +10 | SOL | DOWN | 0.61 | open |  |
| 10-22 13:04 | +5 | SOL | DOWN | 0.61 | 0.67 | 0.27 |
| 10-22 13:03 | +10 stop | ETH | DOWN | 0.67 | 0.50 | -2.04 |
| 10-22 13:03 | +20 | ETH | DOWN | 0.67 | open |  |
| 10-22 13:03 | +15 | ETH | DOWN | 0.67 | open |  |
| 10-22 13:03 | +10 | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 10-22 13:03 | +5 | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 10-22 13:03 | +5 | DOGE | DOWN | 0.55 | 0.62 | 0.35 |
| 10-22 13:03 | +10 stop | BNB | DOWN | 0.71 | 0.87 | 1.37 |
| 10-22 13:03 | +10 stop | BTC | DOWN | 0.64 | 0.41 | -2.64 |
