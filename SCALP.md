# Range-Scalp Bot

*Updated Sun Oct 18 23:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23086 | 20072 | 3014 (30) | 9 | $-6897.41 | -4.7% |
| **+10¢** | 17354 | 13875 | 3479 (44) | 9 | $-6195.20 | -5.7% |
| **+15¢** | 14553 | 10802 | 3751 (66) | 9 | $-5639.57 | -6.2% |
| **+20¢** | 12892 | 8969 | 3923 (84) | 9 | $-5013.84 | -6.2% |
| **+10¢ (15¢ stop)** | 28428 | 28377 | 51 (30) | 0 | $-10884.21 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 23:23 | +5 | SOL | DOWN | 0.57 | open |  |
| 10-18 23:21 | +10 stop | HYPE | UP | 0.63 | 0.80 | 1.41 |
| 10-18 23:21 | +10 stop | ZEC | UP | 0.64 | 0.74 | 0.69 |
| 10-18 23:21 | +10 stop | ETH | UP | 0.64 | 0.78 | 1.10 |
| 10-18 23:21 | +10 stop | SOL | DOWN | 0.68 | 0.32 | -3.92 |
| 10-18 23:21 | +20 | SOL | DOWN | 0.68 | open |  |
| 10-18 23:21 | +15 | SOL | DOWN | 0.68 | open |  |
| 10-18 23:21 | +10 | SOL | DOWN | 0.68 | open |  |
| 10-18 23:21 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 10-18 23:20 | +10 stop | NEAR | UP | 0.61 | 0.85 | 2.14 |
| 10-18 23:20 | +10 stop | BNB | UP | 0.61 | 0.73 | 0.89 |
| 10-18 23:19 | +5 | HYPE | DOWN | 0.61 | open |  |
| 10-18 23:19 | +5 | ETH | DOWN | 0.60 | open |  |
| 10-18 23:19 | +10 stop | BTC | UP | 0.55 | 0.66 | 0.76 |
| 10-18 23:19 | +10 stop | DOGE | UP | 0.58 | 0.73 | 1.18 |
| 10-18 23:19 | +10 stop | BNB | UP | 0.48 | 0.58 | 0.64 |
| 10-18 23:18 | +5 | ETH | DOWN | 0.60 | 0.65 | 0.17 |
| 10-18 23:18 | +10 stop | HYPE | DOWN | 0.60 | 0.42 | -2.15 |
| 10-18 23:18 | +20 | HYPE | DOWN | 0.60 | open |  |
| 10-18 23:18 | +15 | HYPE | DOWN | 0.60 | open |  |
| 10-18 23:18 | +10 | HYPE | DOWN | 0.60 | open |  |
| 10-18 23:18 | +5 | HYPE | DOWN | 0.60 | 0.66 | 0.27 |
| 10-18 23:18 | +10 stop | XRP | DOWN | 0.56 | 0.41 | -1.85 |
| 10-18 23:18 | +20 | XRP | DOWN | 0.54 | open |  |
| 10-18 23:18 | +15 | XRP | DOWN | 0.54 | open |  |
| 10-18 23:18 | +10 | XRP | DOWN | 0.54 | open |  |
| 10-18 23:18 | +5 | XRP | DOWN | 0.54 | open |  |
| 10-18 23:17 | +10 stop | NEAR | DOWN | 0.64 | 0.47 | -2.05 |
| 10-18 23:17 | +20 | NEAR | DOWN | 0.64 | open |  |
| 10-18 23:17 | +15 | NEAR | DOWN | 0.64 | open |  |
| 10-18 23:17 | +10 | NEAR | DOWN | 0.64 | open |  |
| 10-18 23:17 | +5 | NEAR | DOWN | 0.64 | open |  |
| 10-18 23:17 | +5 | BNB | DOWN | 0.67 | open |  |
| 10-18 23:16 | +10 stop | BTC | DOWN | 0.69 | 0.46 | -2.63 |
| 10-18 23:16 | +20 | BTC | DOWN | 0.69 | open |  |
| 10-18 23:16 | +15 | BTC | DOWN | 0.69 | open |  |
| 10-18 23:16 | +10 | BTC | DOWN | 0.69 | open |  |
| 10-18 23:16 | +5 | BTC | DOWN | 0.69 | open |  |
| 10-18 23:16 | +10 stop | DOGE | DOWN | 0.71 | 0.42 | -3.23 |
| 10-18 23:16 | +20 | DOGE | DOWN | 0.71 | open |  |
