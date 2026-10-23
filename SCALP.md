# Range-Scalp Bot

*Updated Fri Oct 23 07:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29969 | 26093 | 3876 (39) | 1 | $-8803.15 | -4.7% |
| **+10¢** | 22469 | 17982 | 4487 (55) | 1 | $-7904.26 | -5.6% |
| **+15¢** | 18815 | 13992 | 4823 (78) | 1 | $-7113.73 | -6.0% |
| **+20¢** | 16656 | 11604 | 5052 (101) | 1 | $-6407.74 | -6.1% |
| **+10¢ (15¢ stop)** | 36767 | 36708 | 59 (32) | 0 | $-13837.98 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 07:55 | +10 stop | HYPE | UP | 0.47 | 0.32 | -1.84 |
| 10-23 07:55 | +5 | HYPE | UP | 0.47 | open |  |
| 10-23 07:52 | +10 stop | HYPE | DOWN | 0.66 | 0.77 | 0.81 |
| 10-23 07:51 | +10 stop | HYPE | DOWN | 0.51 | 0.36 | -1.85 |
| 10-23 07:49 | +5 | BTC | DOWN | 0.65 | 0.70 | 0.19 |
| 10-23 07:49 | +5 | HYPE | UP | 0.60 | 0.71 | 0.74 |
| 10-23 07:49 | +10 stop | XRP | DOWN | 0.60 | 0.73 | 0.99 |
| 10-23 07:47 | +10 stop | ETH | DOWN | 0.68 | 0.82 | 1.13 |
| 10-23 07:47 | +20 | ETH | DOWN | 0.71 | 0.92 | 1.86 |
| 10-23 07:47 | +15 | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 10-23 07:47 | +10 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-23 07:47 | +5 | ETH | DOWN | 0.71 | 0.76 | 0.22 |
| 10-23 07:47 | +10 stop | HYPE | UP | 0.65 | 0.50 | -1.84 |
| 10-23 07:47 | +20 | HYPE | UP | 0.65 | open |  |
| 10-23 07:47 | +15 | HYPE | UP | 0.65 | open |  |
| 10-23 07:47 | +10 | HYPE | UP | 0.65 | open |  |
| 10-23 07:47 | +5 | HYPE | UP | 0.65 | 0.73 | 0.50 |
| 10-23 07:47 | +10 stop | SOL | DOWN | 0.56 | 0.69 | 0.97 |
| 10-23 07:47 | +20 | SOL | DOWN | 0.56 | 0.78 | 1.89 |
| 10-23 07:47 | +15 | SOL | DOWN | 0.56 | 0.78 | 1.89 |
| 10-23 07:47 | +10 | SOL | DOWN | 0.56 | 0.69 | 0.97 |
| 10-23 07:47 | +5 | SOL | DOWN | 0.56 | 0.63 | 0.35 |
| 10-23 07:47 | +10 stop | XRP | DOWN | 0.63 | 0.48 | -1.85 |
| 10-23 07:47 | +20 | XRP | DOWN | 0.63 | 0.84 | 1.83 |
| 10-23 07:47 | +15 | XRP | DOWN | 0.63 | 0.81 | 1.52 |
| 10-23 07:47 | +10 | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-23 07:47 | +5 | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-23 07:47 | +10 stop | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-23 07:47 | +20 | ZEC | DOWN | 0.68 | 0.92 | 2.18 |
| 10-23 07:47 | +15 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-23 07:47 | +10 | ZEC | DOWN | 0.65 | 0.79 | 1.12 |
| 10-23 07:47 | +5 | ZEC | DOWN | 0.65 | 0.71 | 0.29 |
| 10-23 07:46 | +5 | BTC | DOWN | 0.55 | 0.62 | 0.35 |
| 10-23 07:46 | +10 stop | NEAR | DOWN | 0.62 | 0.77 | 1.20 |
| 10-23 07:46 | +20 | NEAR | DOWN | 0.62 | 0.82 | 1.72 |
| 10-23 07:46 | +15 | NEAR | DOWN | 0.62 | 0.77 | 1.20 |
| 10-23 07:46 | +10 | NEAR | DOWN | 0.62 | 0.77 | 1.20 |
| 10-23 07:46 | +5 | NEAR | DOWN | 0.62 | 0.77 | 1.20 |
| 10-23 07:46 | +10 stop | DOGE | DOWN | 0.60 | 0.43 | -2.05 |
| 10-23 07:46 | +20 | DOGE | DOWN | 0.60 | 0.84 | 2.13 |
