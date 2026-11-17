# Range-Scalp Bot

*Updated Tue Nov 17 17:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63061 | 55010 | 8051 (117) | 5 | $-17149.15 | -4.3% |
| **+10¢** | 47107 | 37690 | 9417 (159) | 6 | $-15992.85 | -5.4% |
| **+15¢** | 39488 | 29333 | 10155 (201) | 6 | $-14504.61 | -5.9% |
| **+20¢** | 35185 | 24534 | 10651 (256) | 8 | $-12693.17 | -5.8% |
| **+10¢ (15¢ stop)** | 76747 | 76591 | 156 (92) | 0 | $-28274.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 17:28 | +10 stop | DOGE | DOWN | 0.65 | 0.35 | -3.29 |
| 11-17 17:28 | +15 | DOGE | DOWN | 0.65 | open |  |
| 11-17 17:28 | +10 | DOGE | DOWN | 0.64 | open |  |
| 11-17 17:28 | +5 | DOGE | DOWN | 0.69 | open |  |
| 11-17 17:27 | +10 stop | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 11-17 17:27 | +5 | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 11-17 17:26 | +10 stop | HYPE | UP | 0.46 | 0.67 | 1.76 |
| 11-17 17:25 | +10 stop | ETH | UP | 0.54 | 0.26 | -3.12 |
| 11-17 17:25 | +10 stop | BTC | UP | 0.52 | 0.62 | 0.65 |
| 11-17 17:25 | +10 stop | XRP | UP | 0.55 | 0.29 | -2.93 |
| 11-17 17:25 | +10 stop | NEAR | DOWN | 0.32 | 0.62 | 2.67 |
| 11-17 17:25 | +10 stop | BTC | DOWN | 0.67 | 0.45 | -2.54 |
| 11-17 17:24 | +10 stop | ETH | DOWN | 0.70 | 0.33 | -4.01 |
| 11-17 17:24 | +10 stop | XRP | DOWN | 0.69 | 0.38 | -3.42 |
| 11-17 17:24 | +10 stop | BNB | UP | 0.63 | 0.47 | -1.95 |
| 11-17 17:24 | +20 | BNB | UP | 0.63 | open |  |
| 11-17 17:24 | +15 | BNB | UP | 0.63 | 0.79 | 1.31 |
| 11-17 17:24 | +10 | BNB | UP | 0.62 | 0.79 | 1.41 |
| 11-17 17:24 | +5 | BNB | UP | 0.62 | 0.79 | 1.41 |
| 11-17 17:24 | +10 stop | ZEC | UP | 0.64 | 0.85 | 1.84 |
| 11-17 17:24 | +20 | ZEC | UP | 0.66 | open |  |
| 11-17 17:24 | +15 | ZEC | UP | 0.64 | 0.85 | 1.84 |
| 11-17 17:24 | +10 | ZEC | UP | 0.64 | 0.85 | 1.84 |
| 11-17 17:24 | +5 | ZEC | UP | 0.64 | 0.85 | 1.84 |
| 11-17 17:24 | +10 stop | DOGE | UP | 0.66 | 0.48 | -2.14 |
| 11-17 17:24 | +20 | DOGE | UP | 0.65 | open |  |
| 11-17 17:24 | +15 | DOGE | UP | 0.65 | 0.80 | 1.22 |
| 11-17 17:24 | +10 | DOGE | UP | 0.65 | 0.78 | 1.01 |
| 11-17 17:24 | +5 | DOGE | UP | 0.67 | 0.78 | 0.81 |
| 11-17 17:24 | +10 stop | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 11-17 17:24 | +20 | SOL | DOWN | 0.70 | 0.92 | 2.00 |
| 11-17 17:24 | +15 | SOL | DOWN | 0.70 | 0.92 | 2.00 |
| 11-17 17:24 | +10 | SOL | DOWN | 0.70 | 0.81 | 0.85 |
| 11-17 17:24 | +5 | SOL | DOWN | 0.69 | 0.81 | 0.94 |
| 11-17 17:22 | +10 stop | NEAR | UP | 0.71 | 0.46 | -2.82 |
| 11-17 17:22 | +20 | NEAR | UP | 0.71 | open |  |
| 11-17 17:22 | +15 | NEAR | UP | 0.71 | open |  |
| 11-17 17:22 | +10 | NEAR | UP | 0.71 | open |  |
| 11-17 17:22 | +5 | NEAR | UP | 0.71 | 0.78 | 0.42 |
| 11-17 17:22 | +10 stop | ETH | UP | 0.66 | 0.51 | -1.84 |
