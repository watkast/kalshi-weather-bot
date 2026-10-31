# Range-Scalp Bot

*Updated Sat Oct 31 09:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42057 | 36688 | 5369 (55) | 4 | $-11850.58 | -4.5% |
| **+10¢** | 31354 | 25141 | 6213 (79) | 4 | $-10591.90 | -5.4% |
| **+15¢** | 26215 | 19517 | 6698 (107) | 5 | $-9686.18 | -5.9% |
| **+20¢** | 23281 | 16267 | 7014 (138) | 6 | $-8526.20 | -5.8% |
| **+10¢ (15¢ stop)** | 51273 | 51198 | 75 (41) | 3 | $-19352.94 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 09:32 | +5 | XRP | UP | 0.64 | open |  |
| 10-31 09:32 | +10 stop | NEAR | DOWN | 0.57 | 0.67 | 0.68 |
| 10-31 09:32 | +20 | NEAR | DOWN | 0.57 | open |  |
| 10-31 09:32 | +15 | NEAR | DOWN | 0.55 | open |  |
| 10-31 09:32 | +10 | NEAR | DOWN | 0.55 | 0.67 | 0.86 |
| 10-31 09:32 | +5 | NEAR | DOWN | 0.57 | 0.67 | 0.66 |
| 10-31 09:32 | +10 stop | HYPE | DOWN | 0.61 | 0.73 | 0.85 |
| 10-31 09:32 | +20 | HYPE | DOWN | 0.62 | open |  |
| 10-31 09:32 | +15 | HYPE | DOWN | 0.61 | 0.79 | 1.47 |
| 10-31 09:32 | +10 | HYPE | DOWN | 0.62 | 0.73 | 0.75 |
| 10-31 09:32 | +5 | HYPE | DOWN | 0.62 | 0.73 | 0.75 |
| 10-31 09:31 | +10 stop | ETH | UP | 0.63 | open |  |
| 10-31 09:31 | +20 | ETH | UP | 0.63 | open |  |
| 10-31 09:31 | +15 | ETH | UP | 0.63 | open |  |
| 10-31 09:31 | +10 | ETH | UP | 0.63 | open |  |
| 10-31 09:31 | +5 | ETH | UP | 0.63 | open |  |
| 10-31 09:31 | +10 stop | DOGE | UP | 0.61 | 0.35 | -2.93 |
| 10-31 09:31 | +20 | DOGE | UP | 0.61 | open |  |
| 10-31 09:31 | +15 | DOGE | UP | 0.61 | open |  |
| 10-31 09:31 | +10 | DOGE | UP | 0.61 | open |  |
| 10-31 09:31 | +5 | DOGE | UP | 0.61 | open |  |
| 10-31 09:31 | +10 stop | XRP | UP | 0.65 | open |  |
| 10-31 09:31 | +20 | XRP | UP | 0.65 | open |  |
| 10-31 09:31 | +15 | XRP | UP | 0.65 | open |  |
| 10-31 09:31 | +10 | XRP | UP | 0.64 | open |  |
| 10-31 09:31 | +5 | XRP | UP | 0.64 | 0.72 | 0.48 |
| 10-31 09:31 | +10 stop | BNB | DOWN | 0.52 | open |  |
| 10-31 09:31 | +20 | BNB | DOWN | 0.51 | open |  |
| 10-31 09:31 | +15 | BNB | DOWN | 0.51 | open |  |
| 10-31 09:31 | +10 | BNB | DOWN | 0.51 | open |  |
| 10-31 09:31 | +5 | BNB | DOWN | 0.51 | open |  |
| 10-31 09:28 | +10 stop | NEAR | DOWN | 0.71 | 0.47 | -2.73 |
| 10-31 09:24 | +5 | DOGE | UP | 0.58 | 0.69 | 0.77 |
| 10-31 09:24 | +10 stop | SOL | UP | 0.53 | 0.66 | 0.96 |
| 10-31 09:24 | +20 | SOL | UP | 0.52 | 0.77 | 2.19 |
| 10-31 09:24 | +15 | SOL | UP | 0.51 | 0.66 | 1.16 |
| 10-31 09:24 | +10 | SOL | UP | 0.62 | 0.77 | 1.20 |
| 10-31 09:24 | +10 stop | DOGE | UP | 0.52 | 0.62 | 0.65 |
| 10-31 09:24 | +5 | DOGE | UP | 0.52 | 0.57 | 0.14 |
| 10-31 09:23 | +10 stop | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
