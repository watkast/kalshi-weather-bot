# Range-Scalp Bot

*Updated Sat Oct 31 22:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42808 | 37323 | 5485 (62) | 1 | $-12110.21 | -4.5% |
| **+10¢** | 31920 | 25577 | 6343 (84) | 2 | $-10867.31 | -5.4% |
| **+15¢** | 26706 | 19868 | 6838 (112) | 2 | $-9951.06 | -5.9% |
| **+20¢** | 23716 | 16549 | 7167 (145) | 2 | $-8821.32 | -5.9% |
| **+10¢ (15¢ stop)** | 52222 | 52139 | 83 (48) | 1 | $-19787.88 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 22:09 | +10 stop | HYPE | DOWN | 0.64 | 0.39 | -2.88 |
| 10-31 22:08 | +10 stop | NEAR | DOWN | 0.59 | open |  |
| 10-31 22:08 | +5 | HYPE | DOWN | 0.70 | 0.81 | 0.89 |
| 10-31 22:08 | +10 stop | HYPE | DOWN | 0.50 | 0.64 | 1.05 |
| 10-31 22:08 | +5 | HYPE | DOWN | 0.48 | 0.55 | 0.30 |
| 10-31 22:08 | +10 stop | NEAR | UP | 0.63 | 0.45 | -2.15 |
| 10-31 22:08 | +20 | NEAR | UP | 0.63 | open |  |
| 10-31 22:08 | +15 | NEAR | UP | 0.63 | open |  |
| 10-31 22:08 | +10 | NEAR | UP | 0.63 | open |  |
| 10-31 22:08 | +5 | NEAR | UP | 0.63 | open |  |
| 10-31 22:06 | +10 stop | HYPE | UP | 0.59 | 0.42 | -2.05 |
| 10-31 22:06 | +20 | HYPE | UP | 0.59 | open |  |
| 10-31 22:06 | +15 | HYPE | UP | 0.59 | open |  |
| 10-31 22:06 | +10 | HYPE | UP | 0.59 | open |  |
| 10-31 22:06 | +5 | HYPE | UP | 0.60 | 0.68 | 0.47 |
| 10-31 22:01 | +10 stop | BNB | UP | 0.58 | 0.87 | 2.68 |
| 10-31 22:01 | +20 | BNB | UP | 0.58 | 0.87 | 2.68 |
| 10-31 22:01 | +15 | BNB | UP | 0.58 | 0.87 | 2.68 |
| 10-31 22:01 | +10 | BNB | UP | 0.58 | 0.87 | 2.68 |
| 10-31 22:01 | +5 | BNB | UP | 0.57 | 0.87 | 2.70 |
| 10-31 22:01 | +10 stop | HYPE | DOWN | 0.46 | 0.59 | 0.95 |
| 10-31 22:01 | +10 stop | DOGE | UP | 0.65 | 0.87 | 1.96 |
| 10-31 22:01 | +20 | DOGE | UP | 0.65 | 0.87 | 1.96 |
| 10-31 22:01 | +15 | DOGE | UP | 0.65 | 0.87 | 1.96 |
| 10-31 22:01 | +10 | DOGE | UP | 0.65 | 0.87 | 1.96 |
| 10-31 22:01 | +5 | DOGE | UP | 0.65 | 0.73 | 0.50 |
| 10-31 22:00 | +10 stop | HYPE | UP | 0.55 | 0.36 | -2.25 |
| 10-31 22:00 | +20 | HYPE | UP | 0.55 | 0.75 | 1.68 |
| 10-31 22:00 | +15 | HYPE | UP | 0.55 | 0.70 | 1.17 |
| 10-31 22:00 | +10 | HYPE | UP | 0.55 | 0.70 | 1.17 |
| 10-31 22:00 | +5 | HYPE | UP | 0.55 | 0.70 | 1.17 |
| 10-31 22:00 | +10 stop | ETH | UP | 0.64 | 0.83 | 1.63 |
| 10-31 22:00 | +20 | ETH | UP | 0.64 | 0.91 | 2.50 |
| 10-31 22:00 | +15 | ETH | UP | 0.64 | 0.83 | 1.63 |
| 10-31 22:00 | +10 | ETH | UP | 0.64 | 0.83 | 1.63 |
| 10-31 22:00 | +5 | ETH | UP | 0.64 | 0.73 | 0.59 |
| 10-31 21:58 | +10 stop | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 10-31 21:58 | +20 | XRP | DOWN | 0.66 | 0.88 | 1.96 |
| 10-31 21:58 | +15 | XRP | DOWN | 0.63 | 0.78 | 1.20 |
| 10-31 21:58 | +10 | XRP | DOWN | 0.62 | 0.78 | 1.30 |
