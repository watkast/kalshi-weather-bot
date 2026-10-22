# Range-Scalp Bot

*Updated Thu Oct 22 02:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28146 | 24530 | 3616 (39) | 7 | $-8053.12 | -4.5% |
| **+10¢** | 21137 | 16957 | 4180 (55) | 8 | $-7112.10 | -5.4% |
| **+15¢** | 17704 | 13208 | 4496 (78) | 8 | $-6324.88 | -5.7% |
| **+20¢** | 15667 | 10953 | 4714 (98) | 8 | $-5683.10 | -5.8% |
| **+10¢ (15¢ stop)** | 34544 | 34485 | 59 (32) | 2 | $-12898.64 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 02:54 | +5 | NEAR | UP | 0.58 | open |  |
| 10-22 02:54 | +10 stop | BTC | DOWN | 0.65 | 0.79 | 1.12 |
| 10-22 02:54 | +10 stop | NEAR | UP | 0.55 | open |  |
| 10-22 02:54 | +20 | NEAR | UP | 0.55 | open |  |
| 10-22 02:54 | +15 | NEAR | UP | 0.55 | open |  |
| 10-22 02:54 | +10 | NEAR | UP | 0.55 | open |  |
| 10-22 02:54 | +5 | NEAR | UP | 0.54 | 0.62 | 0.49 |
| 10-22 02:53 | +10 stop | ETH | DOWN | 0.58 | 0.69 | 0.77 |
| 10-22 02:53 | +5 | ETH | DOWN | 0.58 | 0.69 | 0.77 |
| 10-22 02:52 | +5 | BNB | DOWN | 0.69 | 0.78 | 0.62 |
| 10-22 02:52 | +10 stop | BTC | DOWN | 0.56 | 0.72 | 1.27 |
| 10-22 02:51 | +10 stop | ETH | UP | 0.45 | 0.57 | 0.84 |
| 10-22 02:51 | +5 | ETH | UP | 0.45 | 0.57 | 0.84 |
| 10-22 02:51 | +10 stop | DOGE | DOWN | 0.59 | open |  |
| 10-22 02:50 | +10 stop | ZEC | DOWN | 0.60 | 0.76 | 1.30 |
| 10-22 02:50 | +10 stop | BNB | DOWN | 0.62 | 0.78 | 1.30 |
| 10-22 02:50 | +5 | BNB | DOWN | 0.62 | 0.68 | 0.27 |
| 10-22 02:50 | +10 stop | XRP | DOWN | 0.62 | 0.76 | 1.05 |
| 10-22 02:50 | +10 stop | HYPE | DOWN | 0.62 | 0.87 | 2.25 |
| 10-22 02:50 | +10 stop | SOL | DOWN | 0.59 | 0.71 | 0.88 |
| 10-22 02:49 | +5 | BNB | UP | 0.52 | 0.69 | 1.37 |
| 10-22 02:49 | +5 | HYPE | UP | 0.52 | open |  |
| 10-22 02:49 | +10 stop | ZEC | UP | 0.70 | 0.51 | -2.23 |
| 10-22 02:49 | +20 | ZEC | UP | 0.70 | open |  |
| 10-22 02:49 | +5 | DOGE | UP | 0.68 | open |  |
| 10-22 02:48 | +15 | ZEC | UP | 0.71 | open |  |
| 10-22 02:48 | +10 | ZEC | UP | 0.71 | open |  |
| 10-22 02:48 | +5 | ZEC | UP | 0.71 | open |  |
| 10-22 02:48 | +5 | HYPE | UP | 0.57 | 0.63 | 0.21 |
| 10-22 02:48 | +10 stop | HYPE | UP | 0.61 | 0.43 | -2.15 |
| 10-22 02:48 | +5 | BTC | UP | 0.67 | open |  |
| 10-22 02:47 | +5 | HYPE | UP | 0.56 | 0.63 | 0.35 |
| 10-22 02:47 | +10 stop | DOGE | UP | 0.64 | 0.49 | -1.85 |
| 10-22 02:47 | +20 | DOGE | UP | 0.64 | open |  |
| 10-22 02:47 | +15 | DOGE | UP | 0.64 | open |  |
| 10-22 02:47 | +10 | DOGE | UP | 0.64 | open |  |
| 10-22 02:47 | +5 | DOGE | UP | 0.64 | 0.71 | 0.38 |
| 10-22 02:47 | +10 stop | SOL | UP | 0.68 | 0.45 | -2.64 |
| 10-22 02:47 | +20 | SOL | UP | 0.68 | open |  |
| 10-22 02:47 | +15 | SOL | UP | 0.68 | open |  |
