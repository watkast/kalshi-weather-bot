# Range-Scalp Bot

*Updated Sun Oct 11 18:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12302 | 10612 | 1690 (25) | 6 | $-4097.23 | -5.3% |
| **+10¢** | 9342 | 7385 | 1957 (37) | 7 | $-3857.74 | -6.6% |
| **+15¢** | 7870 | 5793 | 2077 (54) | 8 | $-3285.41 | -6.6% |
| **+20¢** | 7016 | 4852 | 2164 (68) | 8 | $-2774.32 | -6.3% |
| **+10¢ (15¢ stop)** | 15168 | 15127 | 41 (25) | 7 | $-5987.58 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 18:35 | +5 | DOGE | DOWN | 0.65 | open |  |
| 10-11 18:35 | +5 | BTC | DOWN | 0.64 | open |  |
| 10-11 18:35 | +10 stop | SOL | UP | 0.59 | open |  |
| 10-11 18:35 | +10 | SOL | UP | 0.59 | open |  |
| 10-11 18:35 | +5 | SOL | UP | 0.59 | open |  |
| 10-11 18:35 | +5 | HYPE | UP | 0.63 | open |  |
| 10-11 18:34 | +5 | BTC | DOWN | 0.57 | 0.63 | 0.25 |
| 10-11 18:34 | +5 | DOGE | DOWN | 0.57 | 0.62 | 0.15 |
| 10-11 18:34 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-11 18:34 | +10 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-11 18:34 | +5 | ETH | DOWN | 0.58 | 0.63 | 0.15 |
| 10-11 18:33 | +10 stop | SOL | UP | 0.61 | 0.74 | 0.99 |
| 10-11 18:33 | +20 | SOL | UP | 0.61 | open |  |
| 10-11 18:33 | +15 | SOL | UP | 0.61 | open |  |
| 10-11 18:33 | +10 | SOL | UP | 0.61 | 0.74 | 0.99 |
| 10-11 18:33 | +5 | SOL | UP | 0.61 | 0.74 | 0.99 |
| 10-11 18:32 | +10 stop | DOGE | DOWN | 0.55 | open |  |
| 10-11 18:32 | +20 | DOGE | DOWN | 0.55 | open |  |
| 10-11 18:32 | +15 | DOGE | DOWN | 0.55 | open |  |
| 10-11 18:32 | +10 | DOGE | DOWN | 0.55 | open |  |
| 10-11 18:32 | +5 | DOGE | DOWN | 0.55 | 0.61 | 0.25 |
| 10-11 18:32 | +5 | XRP | DOWN | 0.59 | 0.73 | 1.09 |
| 10-11 18:32 | +10 stop | BTC | DOWN | 0.61 | open |  |
| 10-11 18:32 | +20 | BTC | DOWN | 0.61 | open |  |
| 10-11 18:32 | +15 | BTC | DOWN | 0.61 | open |  |
| 10-11 18:32 | +10 | BTC | DOWN | 0.61 | open |  |
| 10-11 18:32 | +5 | BTC | DOWN | 0.61 | 0.67 | 0.27 |
| 10-11 18:31 | +10 stop | HYPE | UP | 0.59 | open |  |
| 10-11 18:31 | +20 | HYPE | UP | 0.59 | open |  |
| 10-11 18:31 | +15 | HYPE | UP | 0.59 | open |  |
| 10-11 18:31 | +10 | HYPE | UP | 0.59 | open |  |
| 10-11 18:31 | +5 | HYPE | UP | 0.59 | 0.65 | 0.23 |
| 10-11 18:31 | +10 stop | NEAR | UP | 0.69 | open |  |
| 10-11 18:31 | +20 | NEAR | UP | 0.69 | open |  |
| 10-11 18:31 | +15 | NEAR | UP | 0.69 | open |  |
| 10-11 18:31 | +10 | NEAR | UP | 0.69 | open |  |
| 10-11 18:31 | +5 | NEAR | UP | 0.69 | open |  |
| 10-11 18:31 | +10 stop | XRP | DOWN | 0.50 | 0.63 | 0.97 |
| 10-11 18:31 | +20 | XRP | DOWN | 0.50 | 0.73 | 2.00 |
| 10-11 18:31 | +15 | XRP | DOWN | 0.50 | 0.73 | 2.00 |
