# Range-Scalp Bot

*Updated Tue Nov 24 02:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70435 | 61479 | 8956 (147) | 0 | $-18832.13 | -4.2% |
| **+10¢** | 52549 | 42091 | 10458 (190) | 1 | $-17452.31 | -5.3% |
| **+15¢** | 44022 | 32758 | 11264 (246) | 1 | $-15536.77 | -5.6% |
| **+20¢** | 39200 | 27342 | 11858 (311) | 1 | $-13908.86 | -5.7% |
| **+10¢ (15¢ stop)** | 85766 | 85570 | 196 (118) | 0 | $-31523.86 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 02:03 | +10 stop | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 11-24 02:03 | +5 | XRP | DOWN | 0.71 | 0.84 | 1.05 |
| 11-24 02:02 | +10 stop | ZEC | DOWN | 0.66 | 0.78 | 0.91 |
| 11-24 02:02 | +10 | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 11-24 02:02 | +5 | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 11-24 02:02 | +5 | NEAR | DOWN | 0.61 | 0.78 | 1.40 |
| 11-24 02:02 | +10 stop | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-24 02:02 | +20 | HYPE | DOWN | 0.66 | 0.86 | 1.75 |
| 11-24 02:02 | +15 | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-24 02:02 | +10 | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-24 02:02 | +5 | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-24 02:02 | +10 stop | ETH | DOWN | 0.71 | 0.88 | 1.47 |
| 11-24 02:02 | +20 | ETH | DOWN | 0.70 | 0.96 | 2.40 |
| 11-24 02:02 | +15 | ETH | DOWN | 0.70 | 0.88 | 1.57 |
| 11-24 02:02 | +10 | ETH | DOWN | 0.70 | 0.88 | 1.57 |
| 11-24 02:02 | +5 | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 11-24 02:02 | +10 stop | XRP | DOWN | 0.63 | 0.84 | 1.83 |
| 11-24 02:02 | +20 | XRP | DOWN | 0.63 | 0.84 | 1.83 |
| 11-24 02:02 | +15 | XRP | DOWN | 0.63 | 0.84 | 1.83 |
| 11-24 02:02 | +10 | XRP | DOWN | 0.63 | 0.84 | 1.83 |
| 11-24 02:02 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 11-24 02:01 | +10 stop | DOGE | DOWN | 0.53 | 0.71 | 1.47 |
| 11-24 02:01 | +20 | DOGE | DOWN | 0.53 | 0.73 | 1.68 |
| 11-24 02:01 | +15 | DOGE | DOWN | 0.53 | 0.71 | 1.47 |
| 11-24 02:01 | +10 | DOGE | DOWN | 0.54 | 0.71 | 1.38 |
| 11-24 02:01 | +5 | DOGE | DOWN | 0.54 | 0.71 | 1.37 |
| 11-24 02:01 | +10 stop | NEAR | UP | 0.51 | 0.35 | -1.94 |
| 11-24 02:01 | +20 | NEAR | UP | 0.51 | open |  |
| 11-24 02:01 | +15 | NEAR | UP | 0.51 | open |  |
| 11-24 02:01 | +10 | NEAR | UP | 0.51 | open |  |
| 11-24 02:01 | +5 | NEAR | UP | 0.51 | 0.57 | 0.24 |
| 11-24 02:01 | +10 stop | BNB | DOWN | 0.64 | 0.85 | 1.84 |
| 11-24 02:01 | +20 | BNB | DOWN | 0.64 | 0.85 | 1.84 |
| 11-24 02:01 | +15 | BNB | DOWN | 0.64 | 0.85 | 1.84 |
| 11-24 02:01 | +10 | BNB | DOWN | 0.64 | 0.85 | 1.84 |
| 11-24 02:01 | +5 | BNB | DOWN | 0.64 | 0.69 | 0.18 |
| 11-24 02:01 | +10 stop | ZEC | DOWN | 0.58 | 0.69 | 0.77 |
| 11-24 02:01 | +20 | ZEC | DOWN | 0.58 | 0.78 | 1.69 |
| 11-24 02:01 | +15 | ZEC | DOWN | 0.58 | 0.75 | 1.38 |
| 11-24 02:01 | +10 | ZEC | DOWN | 0.58 | 0.69 | 0.77 |
