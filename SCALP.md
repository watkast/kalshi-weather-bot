# Range-Scalp Bot

*Updated Mon Oct 05 00:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3021 | 2591 | 430 (3) | 6 | $-1102.89 | -5.8% |
| **+10¢** | 2348 | 1863 | 485 (4) | 9 | $-946.32 | -6.4% |
| **+15¢** | 1977 | 1465 | 512 (5) | 8 | $-823.61 | -6.6% |
| **+20¢** | 1764 | 1230 | 534 (10) | 8 | $-692.75 | -6.2% |
| **+10¢ (15¢ stop)** | 3772 | 3771 | 1 (1) | 4 | $-1509.42 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 00:33 | +10 stop | NEAR | UP | 0.70 | open |  |
| 10-05 00:33 | +10 stop | ETH | UP | 0.66 | open |  |
| 10-05 00:33 | +20 | ETH | UP | 0.66 | open |  |
| 10-05 00:33 | +15 | ETH | UP | 0.66 | open |  |
| 10-05 00:33 | +10 | ETH | UP | 0.66 | open |  |
| 10-05 00:33 | +5 | ETH | UP | 0.66 | open |  |
| 10-05 00:32 | +10 stop | DOGE | UP | 0.61 | open |  |
| 10-05 00:32 | +20 | DOGE | UP | 0.61 | open |  |
| 10-05 00:32 | +15 | DOGE | UP | 0.61 | open |  |
| 10-05 00:32 | +10 | DOGE | UP | 0.61 | open |  |
| 10-05 00:32 | +5 | DOGE | UP | 0.61 | 0.69 | 0.48 |
| 10-05 00:32 | +10 stop | HYPE | DOWN | 0.46 | 0.28 | -2.13 |
| 10-05 00:32 | +20 | HYPE | DOWN | 0.46 | open |  |
| 10-05 00:32 | +15 | HYPE | DOWN | 0.46 | open |  |
| 10-05 00:32 | +10 | HYPE | DOWN | 0.46 | open |  |
| 10-05 00:32 | +5 | HYPE | DOWN | 0.46 | 0.55 | 0.54 |
| 10-05 00:31 | +10 stop | BTC | DOWN | 0.67 | open |  |
| 10-05 00:31 | +20 | BTC | DOWN | 0.67 | open |  |
| 10-05 00:31 | +15 | BTC | DOWN | 0.67 | open |  |
| 10-05 00:31 | +10 | BTC | DOWN | 0.67 | open |  |
| 10-05 00:31 | +5 | BTC | DOWN | 0.67 | open |  |
| 10-05 00:31 | +10 | ZEC | DOWN | 0.71 | open |  |
| 10-05 00:31 | +5 | ZEC | DOWN | 0.71 | open |  |
| 10-05 00:31 | +10 stop | XRP | DOWN | 0.58 | 0.43 | -1.87 |
| 10-05 00:31 | +20 | XRP | DOWN | 0.58 | open |  |
| 10-05 00:31 | +15 | XRP | DOWN | 0.58 | open |  |
| 10-05 00:31 | +10 | XRP | DOWN | 0.58 | open |  |
| 10-05 00:31 | +5 | XRP | DOWN | 0.58 | open |  |
| 10-05 00:31 | +10 stop | NEAR | DOWN | 0.63 | 0.47 | -1.95 |
| 10-05 00:31 | +20 | NEAR | DOWN | 0.63 | open |  |
| 10-05 00:31 | +15 | NEAR | DOWN | 0.62 | open |  |
| 10-05 00:31 | +10 | NEAR | DOWN | 0.62 | open |  |
| 10-05 00:31 | +5 | NEAR | DOWN | 0.62 | open |  |
| 10-05 00:31 | +10 stop | SOL | DOWN | 0.66 | 0.51 | -1.84 |
| 10-05 00:31 | +20 | SOL | DOWN | 0.66 | open |  |
| 10-05 00:31 | +15 | SOL | DOWN | 0.66 | open |  |
| 10-05 00:31 | +10 | SOL | DOWN | 0.66 | open |  |
| 10-05 00:31 | +5 | SOL | DOWN | 0.66 | open |  |
| 10-05 00:31 | +10 stop | BNB | UP | 0.57 | 0.41 | -1.95 |
| 10-05 00:31 | +20 | BNB | UP | 0.57 | open |  |
