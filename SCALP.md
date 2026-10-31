# Range-Scalp Bot

*Updated Sat Oct 31 22:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42824 | 37337 | 5487 (62) | 4 | $-12115.78 | -4.5% |
| **+10¢** | 31928 | 25582 | 6346 (84) | 6 | $-10882.46 | -5.4% |
| **+15¢** | 26712 | 19871 | 6841 (112) | 7 | $-9964.60 | -5.9% |
| **+20¢** | 23722 | 16552 | 7170 (145) | 6 | $-8834.24 | -5.9% |
| **+10¢ (15¢ stop)** | 52240 | 52157 | 83 (48) | 1 | $-19802.20 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 22:20 | +10 stop | NEAR | DOWN | 0.53 | 0.36 | -2.05 |
| 10-31 22:20 | +10 stop | XRP | DOWN | 0.58 | 0.41 | -2.05 |
| 10-31 22:19 | +15 | SOL | DOWN | 0.69 | open |  |
| 10-31 22:19 | +5 | SOL | DOWN | 0.69 | 0.78 | 0.62 |
| 10-31 22:19 | +10 stop | HYPE | UP | 0.70 | open |  |
| 10-31 22:19 | +20 | HYPE | UP | 0.70 | open |  |
| 10-31 22:19 | +15 | HYPE | UP | 0.70 | open |  |
| 10-31 22:19 | +10 | HYPE | UP | 0.70 | open |  |
| 10-31 22:19 | +5 | HYPE | UP | 0.70 | open |  |
| 10-31 22:18 | +10 stop | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-31 22:18 | +5 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-31 22:18 | +10 stop | SOL | DOWN | 0.65 | 0.78 | 1.01 |
| 10-31 22:18 | +10 | SOL | DOWN | 0.66 | 0.78 | 0.91 |
| 10-31 22:18 | +5 | DOGE | DOWN | 0.56 | 0.65 | 0.56 |
| 10-31 22:17 | +5 | SOL | DOWN | 0.62 | 0.67 | 0.17 |
| 10-31 22:17 | +5 | ETH | DOWN | 0.62 | 0.72 | 0.68 |
| 10-31 22:17 | +5 | XRP | UP | 0.55 | open |  |
| 10-31 22:17 | +5 | NEAR | UP | 0.61 | open |  |
| 10-31 22:17 | +10 stop | ZEC | DOWN | 0.55 | 0.65 | 0.66 |
| 10-31 22:17 | +10 stop | ETH | UP | 0.45 | 0.27 | -2.12 |
| 10-31 22:17 | +20 | ETH | UP | 0.45 | open |  |
| 10-31 22:17 | +15 | ETH | UP | 0.45 | open |  |
| 10-31 22:17 | +10 | ETH | UP | 0.45 | open |  |
| 10-31 22:17 | +5 | ETH | UP | 0.45 | 0.54 | 0.54 |
| 10-31 22:17 | +10 stop | XRP | UP | 0.55 | 0.39 | -1.95 |
| 10-31 22:17 | +20 | XRP | UP | 0.55 | open |  |
| 10-31 22:17 | +15 | XRP | UP | 0.55 | open |  |
| 10-31 22:17 | +10 | XRP | UP | 0.55 | open |  |
| 10-31 22:17 | +5 | XRP | UP | 0.55 | 0.62 | 0.35 |
| 10-31 22:17 | +10 stop | DOGE | UP | 0.47 | 0.32 | -1.84 |
| 10-31 22:17 | +20 | DOGE | UP | 0.47 | open |  |
| 10-31 22:17 | +15 | DOGE | UP | 0.47 | open |  |
| 10-31 22:17 | +10 | DOGE | UP | 0.47 | open |  |
| 10-31 22:17 | +5 | DOGE | UP | 0.47 | 0.56 | 0.54 |
| 10-31 22:17 | +5 | BTC | DOWN | 0.62 | 0.75 | 0.99 |
| 10-31 22:16 | +10 stop | BTC | DOWN | 0.55 | 0.65 | 0.66 |
| 10-31 22:16 | +10 | BTC | DOWN | 0.55 | 0.65 | 0.66 |
| 10-31 22:16 | +5 | BTC | DOWN | 0.56 | 0.63 | 0.35 |
| 10-31 22:16 | +10 stop | BNB | UP | 0.66 | 0.49 | -2.04 |
| 10-31 22:16 | +20 | BNB | UP | 0.66 | open |  |
