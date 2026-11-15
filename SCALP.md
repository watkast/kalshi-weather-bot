# Range-Scalp Bot

*Updated Sun Nov 15 01:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60162 | 52480 | 7682 (107) | 6 | $-16370.10 | -4.3% |
| **+10¢** | 44950 | 35948 | 9002 (143) | 7 | $-15452.70 | -5.5% |
| **+15¢** | 37664 | 27957 | 9707 (181) | 8 | $-14089.82 | -6.0% |
| **+20¢** | 33562 | 23378 | 10184 (233) | 8 | $-12418.03 | -5.9% |
| **+10¢ (15¢ stop)** | 73266 | 73123 | 143 (82) | 3 | $-26988.08 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 01:53 | +10 stop | BNB | UP | 0.55 | 0.66 | 0.76 |
| 11-15 01:53 | +20 | BNB | UP | 0.56 | open |  |
| 11-15 01:53 | +15 | BNB | UP | 0.58 | open |  |
| 11-15 01:53 | +10 | BNB | UP | 0.58 | 0.71 | 0.99 |
| 11-15 01:53 | +5 | BNB | UP | 0.58 | 0.66 | 0.48 |
| 11-15 01:53 | +10 stop | BTC | UP | 0.51 | 0.64 | 0.95 |
| 11-15 01:53 | +10 stop | NEAR | DOWN | 0.70 | open |  |
| 11-15 01:53 | +10 stop | DOGE | UP | 0.67 | 0.41 | -2.93 |
| 11-15 01:52 | +15 | SOL | DOWN | 0.71 | open |  |
| 11-15 01:52 | +10 | SOL | DOWN | 0.71 | open |  |
| 11-15 01:52 | +10 stop | ZEC | UP | 0.70 | open |  |
| 11-15 01:52 | +5 | ZEC | UP | 0.70 | open |  |
| 11-15 01:52 | +10 stop | XRP | UP | 0.58 | 0.39 | -2.25 |
| 11-15 01:52 | +10 stop | SOL | DOWN | 0.70 | open |  |
| 11-15 01:52 | +5 | SOL | DOWN | 0.70 | 0.78 | 0.52 |
| 11-15 01:52 | +10 stop | HYPE | UP | 0.50 | 0.34 | -1.94 |
| 11-15 01:52 | +10 stop | SOL | UP | 0.41 | 0.55 | 1.05 |
| 11-15 01:52 | +5 | SOL | UP | 0.41 | 0.55 | 1.05 |
| 11-15 01:50 | +5 | SOL | UP | 0.58 | 0.76 | 1.45 |
| 11-15 01:50 | +10 stop | NEAR | UP | 0.66 | 0.84 | 1.54 |
| 11-15 01:49 | +10 stop | HYPE | DOWN | 0.56 | 0.23 | -3.61 |
| 11-15 01:49 | +10 stop | NEAR | DOWN | 0.47 | 0.58 | 0.74 |
| 11-15 01:49 | +10 stop | SOL | DOWN | 0.51 | 0.35 | -1.94 |
| 11-15 01:49 | +20 | SOL | DOWN | 0.51 | 0.72 | 1.77 |
| 11-15 01:49 | +15 | SOL | DOWN | 0.51 | 0.66 | 1.16 |
| 11-15 01:49 | +10 | SOL | DOWN | 0.51 | 0.66 | 1.16 |
| 11-15 01:49 | +5 | SOL | DOWN | 0.51 | 0.57 | 0.24 |
| 11-15 01:48 | +10 stop | ZEC | UP | 0.64 | 0.87 | 2.05 |
| 11-15 01:48 | +10 stop | HYPE | UP | 0.50 | 0.34 | -1.94 |
| 11-15 01:48 | +10 stop | NEAR | UP | 0.58 | 0.42 | -1.96 |
| 11-15 01:47 | +5 | ZEC | UP | 0.68 | 0.73 | 0.20 |
| 11-15 01:47 | +10 stop | BNB | UP | 0.70 | 0.81 | 0.84 |
| 11-15 01:47 | +20 | BNB | UP | 0.70 | 0.93 | 2.05 |
| 11-15 01:47 | +15 | BNB | UP | 0.71 | 0.93 | 1.95 |
| 11-15 01:47 | +10 | BNB | UP | 0.71 | 0.81 | 0.74 |
| 11-15 01:47 | +5 | BNB | UP | 0.71 | 0.81 | 0.76 |
| 11-15 01:47 | +10 stop | XRP | UP | 0.66 | 0.78 | 0.91 |
| 11-15 01:47 | +10 stop | ETH | UP | 0.65 | 0.82 | 1.43 |
| 11-15 01:47 | +10 stop | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 11-15 01:47 | +10 stop | BTC | UP | 0.61 | 0.71 | 0.68 |
