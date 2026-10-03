# Range-Scalp Bot

*Updated Sat Oct 03 06:48 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 338 | 287 | 51 (1) | 7 | $-145.79 | -6.8% |
| **+10¢** | 272 | 216 | 56 (1) | 8 | $-115.87 | -6.7% |
| **+15¢** | 228 | 168 | 60 (1) | 8 | $-117.57 | -8.2% |
| **+20¢** | 417 | 287 | 130 (2) | 8 | $-207.65 | -7.9% |
| **+10¢ (15¢ stop)** | 465 | 465 | 0 (0) | 5 | $-234.16 | -8.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 06:48 | +10 stop | XRP | UP | 0.70 | 0.55 | -1.83 |
| 10-03 06:48 | +10 stop | ETH | UP | 0.56 | open |  |
| 10-03 06:47 | +10 stop | DOGE | UP | 0.68 | open |  |
| 10-03 06:47 | +10 stop | ZEC | UP | 0.59 | open |  |
| 10-03 06:47 | +10 stop | BNB | DOWN | 0.60 | open |  |
| 10-03 06:47 | +20 | BNB | DOWN | 0.60 | open |  |
| 10-03 06:47 | +15 | BNB | DOWN | 0.61 | open |  |
| 10-03 06:47 | +10 | BNB | DOWN | 0.61 | open |  |
| 10-03 06:47 | +5 | BNB | DOWN | 0.61 | open |  |
| 10-03 06:47 | +10 stop | XRP | DOWN | 0.59 | 0.42 | -2.05 |
| 10-03 06:47 | +20 | XRP | DOWN | 0.59 | open |  |
| 10-03 06:47 | +15 | XRP | DOWN | 0.59 | open |  |
| 10-03 06:47 | +10 | XRP | DOWN | 0.59 | open |  |
| 10-03 06:47 | +5 | XRP | DOWN | 0.59 | open |  |
| 10-03 06:46 | +10 stop | BTC | DOWN | 0.68 | open |  |
| 10-03 06:46 | +20 | BTC | DOWN | 0.68 | open |  |
| 10-03 06:46 | +15 | BTC | DOWN | 0.68 | open |  |
| 10-03 06:46 | +10 | BTC | DOWN | 0.68 | open |  |
| 10-03 06:46 | +5 | BTC | DOWN | 0.68 | open |  |
| 10-03 06:46 | +10 stop | NEAR | DOWN | 0.58 | 0.35 | -2.63 |
| 10-03 06:46 | +20 | NEAR | DOWN | 0.57 | open |  |
| 10-03 06:46 | +15 | NEAR | DOWN | 0.58 | open |  |
| 10-03 06:46 | +10 | NEAR | DOWN | 0.57 | open |  |
| 10-03 06:46 | +5 | NEAR | DOWN | 0.57 | 0.63 | 0.23 |
| 10-03 06:46 | +10 stop | DOGE | DOWN | 0.62 | 0.43 | -2.25 |
| 10-03 06:46 | +20 | DOGE | DOWN | 0.62 | open |  |
| 10-03 06:46 | +15 | DOGE | DOWN | 0.62 | open |  |
| 10-03 06:46 | +10 | DOGE | DOWN | 0.62 | open |  |
| 10-03 06:46 | +5 | DOGE | DOWN | 0.62 | open |  |
| 10-03 06:46 | +10 stop | ZEC | DOWN | 0.57 | 0.40 | -2.05 |
| 10-03 06:46 | +20 | ZEC | DOWN | 0.57 | open |  |
| 10-03 06:46 | +15 | ZEC | DOWN | 0.57 | open |  |
| 10-03 06:46 | +10 | ZEC | DOWN | 0.57 | open |  |
| 10-03 06:46 | +5 | ZEC | DOWN | 0.57 | open |  |
| 10-03 06:46 | +10 stop | ETH | DOWN | 0.65 | 0.49 | -1.94 |
| 10-03 06:46 | +20 | ETH | DOWN | 0.65 | open |  |
| 10-03 06:46 | +15 | ETH | DOWN | 0.65 | open |  |
| 10-03 06:46 | +10 | ETH | DOWN | 0.65 | open |  |
| 10-03 06:46 | +5 | ETH | DOWN | 0.65 | open |  |
| 10-03 06:46 | +10 stop | SOL | DOWN | 0.66 | 0.49 | -2.04 |
