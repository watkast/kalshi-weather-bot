# Range-Scalp Bot

*Updated Wed Oct 07 05:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5992 | 5198 | 794 (9) | 2 | $-1821.55 | -4.8% |
| **+10¢** | 4571 | 3636 | 935 (16) | 2 | $-1706.44 | -5.9% |
| **+15¢** | 3840 | 2849 | 991 (20) | 2 | $-1472.06 | -6.1% |
| **+20¢** | 3426 | 2390 | 1036 (27) | 4 | $-1226.69 | -5.7% |
| **+10¢ (15¢ stop)** | 7273 | 7258 | 15 (9) | 2 | $-2520.59 | -5.5% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 05:06 | +10 | BTC | UP | 0.66 | open |  |
| 10-07 05:06 | +10 stop | BTC | UP | 0.65 | open |  |
| 10-07 05:05 | +5 | ETH | UP | 0.65 | open |  |
| 10-07 05:05 | +10 stop | ETH | UP | 0.66 | open |  |
| 10-07 05:05 | +10 stop | ETH | DOWN | 0.47 | 0.61 | 1.05 |
| 10-07 05:05 | +10 stop | BTC | DOWN | 0.46 | 0.61 | 1.15 |
| 10-07 05:04 | +5 | ETH | UP | 0.57 | 0.64 | 0.35 |
| 10-07 05:04 | +10 stop | ETH | UP | 0.58 | 0.42 | -1.96 |
| 10-07 05:04 | +10 | ETH | UP | 0.59 | open |  |
| 10-07 05:04 | +5 | ETH | UP | 0.59 | 0.65 | 0.27 |
| 10-07 05:03 | +5 | BTC | UP | 0.66 | open |  |
| 10-07 05:01 | +10 stop | ETH | UP | 0.62 | 0.73 | 0.79 |
| 10-07 05:01 | +20 | ETH | UP | 0.62 | open |  |
| 10-07 05:01 | +15 | ETH | UP | 0.62 | open |  |
| 10-07 05:01 | +10 | ETH | UP | 0.62 | 0.73 | 0.79 |
| 10-07 05:01 | +5 | ETH | UP | 0.62 | 0.69 | 0.38 |
| 10-07 05:01 | +10 stop | BTC | UP | 0.57 | 0.42 | -1.86 |
| 10-07 05:01 | +20 | BTC | UP | 0.57 | open |  |
| 10-07 05:01 | +15 | BTC | UP | 0.57 | open |  |
| 10-07 05:01 | +10 | BTC | UP | 0.57 | 0.68 | 0.76 |
| 10-07 05:01 | +5 | BTC | UP | 0.57 | 0.62 | 0.15 |
| 10-07 05:01 | +10 stop | BNB | UP | 0.68 | 0.80 | 0.92 |
| 10-07 05:01 | +20 | BNB | UP | 0.68 | 0.91 | 2.06 |
| 10-07 05:01 | +15 | BNB | UP | 0.68 | 0.85 | 1.45 |
| 10-07 05:01 | +10 | BNB | UP | 0.68 | 0.80 | 0.92 |
| 10-07 05:01 | +5 | BNB | UP | 0.68 | 0.80 | 0.92 |
| 10-07 05:01 | +10 stop | HYPE | UP | 0.68 | 0.85 | 1.45 |
| 10-07 05:01 | +20 | HYPE | UP | 0.68 | 0.89 | 1.87 |
| 10-07 05:01 | +15 | HYPE | UP | 0.68 | 0.85 | 1.45 |
| 10-07 05:01 | +10 | HYPE | UP | 0.68 | 0.85 | 1.45 |
| 10-07 05:01 | +5 | HYPE | UP | 0.68 | 0.73 | 0.20 |
| 10-07 05:00 | +10 stop | XRP | UP | 0.71 | 0.81 | 0.77 |
| 10-07 05:00 | +20 | XRP | UP | 0.71 | open |  |
| 10-07 05:00 | +15 | XRP | UP | 0.71 | 0.88 | 1.51 |
| 10-07 05:00 | +10 | XRP | UP | 0.71 | 0.81 | 0.78 |
| 10-07 05:00 | +5 | XRP | UP | 0.69 | 0.78 | 0.65 |
| 10-07 05:00 | +10 stop | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 10-07 05:00 | +20 | DOGE | UP | 0.68 | open |  |
| 10-07 05:00 | +15 | DOGE | UP | 0.68 | 0.84 | 1.34 |
| 10-07 05:00 | +10 | DOGE | UP | 0.68 | 0.78 | 0.71 |
