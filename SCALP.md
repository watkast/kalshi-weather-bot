# Range-Scalp Bot

*Updated Wed Oct 21 00:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26420 | 23011 | 3409 (33) | 4 | $-7704.68 | -4.6% |
| **+10¢** | 19876 | 15941 | 3935 (48) | 6 | $-6785.89 | -5.4% |
| **+15¢** | 16635 | 12402 | 4233 (72) | 7 | $-6035.31 | -5.8% |
| **+20¢** | 14719 | 10279 | 4440 (91) | 8 | $-5438.64 | -5.9% |
| **+10¢ (15¢ stop)** | 32365 | 32312 | 53 (30) | 1 | $-11827.84 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 00:07 | +10 stop | NEAR | DOWN | 0.70 | open |  |
| 10-21 00:07 | +5 | NEAR | DOWN | 0.70 | 0.79 | 0.63 |
| 10-21 00:06 | +10 stop | DOGE | DOWN | 0.51 | 0.65 | 1.06 |
| 10-21 00:06 | +10 stop | SOL | DOWN | 0.57 | 0.74 | 1.38 |
| 10-21 00:06 | +10 stop | HYPE | UP | 0.62 | 0.76 | 1.10 |
| 10-21 00:05 | +10 stop | ETH | DOWN | 0.62 | 0.76 | 1.10 |
| 10-21 00:05 | +20 | ETH | DOWN | 0.62 | open |  |
| 10-21 00:05 | +15 | ETH | DOWN | 0.62 | 0.81 | 1.62 |
| 10-21 00:05 | +10 | ETH | DOWN | 0.62 | 0.76 | 1.10 |
| 10-21 00:05 | +5 | ETH | DOWN | 0.62 | 0.67 | 0.17 |
| 10-21 00:05 | +10 stop | BTC | DOWN | 0.67 | 0.82 | 1.23 |
| 10-21 00:05 | +20 | BTC | DOWN | 0.67 | 0.87 | 1.76 |
| 10-21 00:05 | +15 | BTC | DOWN | 0.67 | 0.82 | 1.23 |
| 10-21 00:05 | +10 | BTC | DOWN | 0.67 | 0.82 | 1.23 |
| 10-21 00:05 | +5 | BTC | DOWN | 0.67 | 0.82 | 1.23 |
| 10-21 00:05 | +10 stop | ZEC | UP | 0.69 | 0.80 | 0.83 |
| 10-21 00:05 | +10 stop | SOL | DOWN | 0.65 | 0.50 | -1.84 |
| 10-21 00:05 | +20 | SOL | DOWN | 0.65 | open |  |
| 10-21 00:05 | +15 | SOL | DOWN | 0.65 | open |  |
| 10-21 00:05 | +10 | SOL | DOWN | 0.65 | open |  |
| 10-21 00:05 | +5 | SOL | DOWN | 0.65 | 0.74 | 0.60 |
| 10-21 00:05 | +10 stop | DOGE | DOWN | 0.70 | 0.50 | -2.33 |
| 10-21 00:05 | +20 | DOGE | DOWN | 0.70 | open |  |
| 10-21 00:05 | +15 | DOGE | DOWN | 0.70 | open |  |
| 10-21 00:05 | +10 | DOGE | DOWN | 0.70 | open |  |
| 10-21 00:05 | +5 | DOGE | DOWN | 0.70 | open |  |
| 10-21 00:04 | +5 | XRP | DOWN | 0.66 | open |  |
| 10-21 00:04 | +5 | XRP | DOWN | 0.53 | 0.62 | 0.55 |
| 10-21 00:03 | +10 stop | HYPE | DOWN | 0.60 | 0.45 | -1.85 |
| 10-21 00:03 | +5 | HYPE | DOWN | 0.60 | open |  |
| 10-21 00:03 | +10 stop | ZEC | DOWN | 0.60 | 0.35 | -2.83 |
| 10-21 00:03 | +20 | ZEC | DOWN | 0.60 | open |  |
| 10-21 00:03 | +15 | ZEC | DOWN | 0.60 | open |  |
| 10-21 00:03 | +10 | ZEC | DOWN | 0.60 | open |  |
| 10-21 00:03 | +5 | ZEC | DOWN | 0.60 | open |  |
| 10-21 00:03 | +10 stop | XRP | DOWN | 0.63 | 0.46 | -2.05 |
| 10-21 00:03 | +20 | XRP | DOWN | 0.63 | open |  |
| 10-21 00:03 | +15 | XRP | DOWN | 0.61 | open |  |
| 10-21 00:03 | +10 | XRP | DOWN | 0.61 | open |  |
| 10-21 00:03 | +5 | XRP | DOWN | 0.62 | 0.67 | 0.17 |
