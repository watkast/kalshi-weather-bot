# Range-Scalp Bot

*Updated Mon Oct 19 09:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23794 | 20687 | 3107 (31) | 3 | $-7104.92 | -4.7% |
| **+10¢** | 17901 | 14319 | 3582 (45) | 3 | $-6346.18 | -5.6% |
| **+15¢** | 14996 | 11140 | 3856 (67) | 3 | $-5744.65 | -6.1% |
| **+20¢** | 13278 | 9245 | 4033 (86) | 3 | $-5092.72 | -6.1% |
| **+10¢ (15¢ stop)** | 29278 | 29227 | 51 (30) | 3 | $-11062.67 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 09:31 | +10 stop | HYPE | UP | 0.61 | open |  |
| 10-19 09:31 | +20 | HYPE | UP | 0.61 | open |  |
| 10-19 09:31 | +15 | HYPE | UP | 0.61 | open |  |
| 10-19 09:31 | +10 | HYPE | UP | 0.61 | open |  |
| 10-19 09:31 | +5 | HYPE | UP | 0.61 | open |  |
| 10-19 09:30 | +10 stop | SOL | UP | 0.58 | open |  |
| 10-19 09:30 | +20 | SOL | UP | 0.58 | open |  |
| 10-19 09:30 | +15 | SOL | UP | 0.58 | open |  |
| 10-19 09:30 | +10 | SOL | UP | 0.58 | open |  |
| 10-19 09:30 | +5 | SOL | UP | 0.58 | open |  |
| 10-19 09:30 | +10 stop | ETH | UP | 0.66 | open |  |
| 10-19 09:30 | +20 | ETH | UP | 0.66 | open |  |
| 10-19 09:30 | +15 | ETH | UP | 0.66 | open |  |
| 10-19 09:30 | +10 | ETH | UP | 0.66 | open |  |
| 10-19 09:30 | +5 | ETH | UP | 0.66 | open |  |
| 10-19 09:23 | +10 stop | NEAR | UP | 0.71 | 0.83 | 0.95 |
| 10-19 09:20 | +10 stop | NEAR | UP | 0.71 | 0.85 | 1.16 |
| 10-19 09:19 | +10 stop | XRP | UP | 0.71 | 0.81 | 0.74 |
| 10-19 09:19 | +5 | BTC | UP | 0.71 | 0.77 | 0.32 |
| 10-19 09:18 | +10 stop | NEAR | UP | 0.52 | 0.68 | 1.26 |
| 10-19 09:18 | +10 stop | BTC | UP | 0.64 | 0.77 | 1.00 |
| 10-19 09:17 | +5 | XRP | UP | 0.71 | 0.81 | 0.74 |
| 10-19 09:17 | +5 | BTC | UP | 0.62 | 0.71 | 0.58 |
| 10-19 09:17 | +5 | ZEC | UP | 0.67 | 0.73 | 0.30 |
| 10-19 09:17 | +10 stop | ETH | UP | 0.68 | 0.79 | 0.82 |
| 10-19 09:17 | +20 | ETH | UP | 0.68 | 0.88 | 1.76 |
| 10-19 09:17 | +15 | ETH | UP | 0.68 | 0.86 | 1.55 |
| 10-19 09:17 | +10 | ETH | UP | 0.68 | 0.79 | 0.82 |
| 10-19 09:17 | +5 | ETH | UP | 0.68 | 0.79 | 0.82 |
| 10-19 09:17 | +5 | ZEC | DOWN | 0.48 | 0.54 | 0.24 |
| 10-19 09:16 | +10 stop | XRP | DOWN | 0.49 | 0.34 | -1.84 |
| 10-19 09:16 | +20 | XRP | DOWN | 0.49 | yes | -5.08 |
| 10-19 09:16 | +15 | XRP | DOWN | 0.49 | yes | -5.08 |
| 10-19 09:16 | +10 | XRP | DOWN | 0.49 | yes | -5.08 |
| 10-19 09:16 | +5 | XRP | DOWN | 0.49 | 0.54 | 0.14 |
| 10-19 09:16 | +5 | BTC | DOWN | 0.50 | 0.57 | 0.34 |
| 10-19 09:16 | +10 stop | DOGE | DOWN | 0.55 | 0.38 | -2.03 |
| 10-19 09:16 | +20 | DOGE | DOWN | 0.55 | yes | -5.66 |
| 10-19 09:16 | +15 | DOGE | DOWN | 0.55 | yes | -5.66 |
| 10-19 09:16 | +10 | DOGE | DOWN | 0.55 | yes | -5.66 |
