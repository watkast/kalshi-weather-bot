# Range-Scalp Bot

*Updated Sun Nov 15 04:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60368 | 52653 | 7715 (107) | 2 | $-16463.04 | -4.3% |
| **+10¢** | 45104 | 36064 | 9040 (143) | 2 | $-15549.74 | -5.5% |
| **+15¢** | 37781 | 28033 | 9748 (181) | 2 | $-14215.21 | -6.0% |
| **+20¢** | 33676 | 23450 | 10226 (233) | 2 | $-12520.64 | -5.9% |
| **+10¢ (15¢ stop)** | 73513 | 73370 | 143 (82) | 0 | $-27097.63 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 04:37 | +10 stop | XRP | UP | 0.51 | 0.34 | -2.04 |
| 11-15 04:37 | +10 | XRP | UP | 0.52 | open |  |
| 11-15 04:37 | +5 | XRP | UP | 0.51 | open |  |
| 11-15 04:37 | +10 stop | SOL | UP | 0.13 | 0.53 | 3.74 |
| 11-15 04:37 | +10 stop | BTC | UP | 0.63 | 0.25 | -4.11 |
| 11-15 04:36 | +10 stop | DOGE | DOWN | 0.56 | 0.77 | 1.79 |
| 11-15 04:35 | +10 stop | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 11-15 04:35 | +20 | NEAR | DOWN | 0.71 | 0.92 | 1.91 |
| 11-15 04:35 | +15 | NEAR | DOWN | 0.71 | 0.86 | 1.26 |
| 11-15 04:35 | +10 | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 11-15 04:35 | +5 | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 11-15 04:35 | +10 stop | XRP | UP | 0.66 | 0.77 | 0.81 |
| 11-15 04:35 | +10 | XRP | UP | 0.66 | 0.77 | 0.81 |
| 11-15 04:35 | +5 | XRP | UP | 0.66 | 0.72 | 0.29 |
| 11-15 04:35 | +10 stop | ETH | UP | 0.62 | 0.31 | -3.42 |
| 11-15 04:35 | +20 | ETH | UP | 0.62 | open |  |
| 11-15 04:35 | +15 | ETH | UP | 0.62 | open |  |
| 11-15 04:35 | +10 | ETH | UP | 0.62 | open |  |
| 11-15 04:35 | +5 | ETH | UP | 0.63 | open |  |
| 11-15 04:35 | +10 stop | SOL | UP | 0.64 | 0.49 | -1.85 |
| 11-15 04:34 | +10 stop | DOGE | UP | 0.67 | 0.44 | -2.64 |
| 11-15 04:34 | +10 stop | BTC | UP | 0.63 | 0.48 | -1.85 |
| 11-15 04:34 | +10 stop | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-15 04:34 | +10 | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-15 04:34 | +5 | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-15 04:34 | +10 stop | BNB | DOWN | 0.52 | 0.79 | 2.40 |
| 11-15 04:34 | +5 | ETH | UP | 0.60 | 0.77 | 1.40 |
| 11-15 04:33 | +10 stop | ETH | UP | 0.58 | 0.77 | 1.59 |
| 11-15 04:33 | +10 stop | ETH | DOWN | 0.45 | 0.58 | 0.94 |
| 11-15 04:32 | +5 | BTC | DOWN | 0.66 | 0.74 | 0.50 |
| 11-15 04:32 | +10 stop | BTC | DOWN | 0.59 | 0.33 | -2.93 |
| 11-15 04:32 | +20 | BTC | DOWN | 0.59 | 0.79 | 1.71 |
| 11-15 04:32 | +15 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-15 04:32 | +10 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-15 04:32 | +5 | BTC | DOWN | 0.59 | 0.66 | 0.37 |
| 11-15 04:32 | +10 stop | BNB | DOWN | 0.70 | 0.54 | -1.93 |
| 11-15 04:32 | +20 | BNB | DOWN | 0.70 | 0.90 | 1.78 |
| 11-15 04:32 | +15 | BNB | DOWN | 0.70 | 0.85 | 1.26 |
| 11-15 04:32 | +10 | BNB | DOWN | 0.70 | 0.84 | 1.15 |
| 11-15 04:32 | +5 | BNB | DOWN | 0.70 | 0.79 | 0.63 |
