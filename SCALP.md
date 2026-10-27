# Range-Scalp Bot

*Updated Tue Oct 27 16:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36795 | 32128 | 4667 (43) | 2 | $-10219.93 | -4.4% |
| **+10¢** | 27485 | 22078 | 5407 (65) | 2 | $-9100.81 | -5.3% |
| **+15¢** | 22997 | 17194 | 5803 (89) | 2 | $-8031.36 | -5.6% |
| **+20¢** | 20384 | 14309 | 6075 (114) | 2 | $-7012.80 | -5.5% |
| **+10¢ (15¢ stop)** | 45086 | 45022 | 64 (33) | 0 | $-17178.89 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 16:57 | +10 stop | SOL | UP | 0.70 | 0.98 | 2.61 |
| 10-27 16:57 | +10 stop | NEAR | DOWN | 0.67 | 0.47 | -2.34 |
| 10-27 16:56 | +5 | NEAR | UP | 0.55 | 0.87 | 2.94 |
| 10-27 16:56 | +10 | SOL | UP | 0.68 | 0.98 | 2.80 |
| 10-27 16:56 | +10 stop | NEAR | UP | 0.55 | 0.35 | -2.34 |
| 10-27 16:55 | +5 | SOL | UP | 0.68 | 0.98 | 2.80 |
| 10-27 16:55 | +10 stop | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-27 16:55 | +10 stop | SOL | UP | 0.61 | 0.72 | 0.78 |
| 10-27 16:55 | +10 stop | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 10-27 16:55 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
| 10-27 16:55 | +10 stop | DOGE | DOWN | 0.39 | 0.57 | 1.45 |
| 10-27 16:55 | +5 | DOGE | DOWN | 0.39 | 0.57 | 1.45 |
| 10-27 16:54 | +10 stop | HYPE | UP | 0.60 | 0.70 | 0.68 |
| 10-27 16:54 | +10 | HYPE | UP | 0.59 | 0.70 | 0.78 |
| 10-27 16:54 | +5 | HYPE | UP | 0.59 | 0.70 | 0.78 |
| 10-27 16:53 | +10 stop | ZEC | UP | 0.32 | 0.62 | 2.67 |
| 10-27 16:52 | +10 stop | ZEC | DOWN | 0.60 | 0.37 | -2.60 |
| 10-27 16:52 | +10 stop | HYPE | UP | 0.65 | 0.79 | 1.12 |
| 10-27 16:52 | +15 | HYPE | UP | 0.65 | 0.86 | 1.85 |
| 10-27 16:52 | +10 | HYPE | UP | 0.65 | 0.79 | 1.12 |
| 10-27 16:52 | +5 | HYPE | UP | 0.65 | 0.70 | 0.19 |
| 10-27 16:52 | +10 stop | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 10-27 16:51 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-27 16:49 | +10 stop | DOGE | DOWN | 0.65 | 0.50 | -1.84 |
| 10-27 16:49 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-27 16:49 | +10 stop | ZEC | DOWN | 0.53 | 0.69 | 1.27 |
| 10-27 16:48 | +10 stop | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 10-27 16:48 | +10 stop | ZEC | DOWN | 0.49 | 0.61 | 0.85 |
| 10-27 16:48 | +10 stop | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-27 16:48 | +10 stop | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 10-27 16:47 | +10 stop | HYPE | UP | 0.65 | 0.80 | 1.22 |
| 10-27 16:47 | +20 | HYPE | UP | 0.65 | 0.86 | 1.85 |
| 10-27 16:47 | +15 | HYPE | UP | 0.64 | 0.80 | 1.31 |
| 10-27 16:47 | +10 | HYPE | UP | 0.64 | 0.80 | 1.31 |
| 10-27 16:47 | +5 | HYPE | UP | 0.64 | 0.70 | 0.28 |
| 10-27 16:47 | +10 stop | BTC | DOWN | 0.68 | 0.80 | 0.92 |
| 10-27 16:47 | +20 | BTC | DOWN | 0.68 | 0.91 | 2.11 |
| 10-27 16:47 | +15 | BTC | DOWN | 0.68 | 0.91 | 2.11 |
| 10-27 16:47 | +10 | BTC | DOWN | 0.68 | 0.80 | 0.92 |
| 10-27 16:47 | +5 | BTC | DOWN | 0.68 | 0.74 | 0.30 |
