# Range-Scalp Bot

*Updated Wed Oct 14 19:47 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16433 | 14236 | 2197 (28) | 5 | $-5199.77 | -5.0% |
| **+10¢** | 12429 | 9883 | 2546 (40) | 8 | $-4781.55 | -6.1% |
| **+15¢** | 10448 | 7716 | 2732 (59) | 8 | $-4276.78 | -6.5% |
| **+20¢** | 9290 | 6426 | 2864 (76) | 9 | $-3788.53 | -6.5% |
| **+10¢ (15¢ stop)** | 20239 | 20189 | 50 (29) | 8 | $-7807.66 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 19:47 | +10 stop | ZEC | DOWN | 0.60 | open |  |
| 10-14 19:47 | +20 | ZEC | DOWN | 0.60 | open |  |
| 10-14 19:47 | +15 | ZEC | DOWN | 0.60 | open |  |
| 10-14 19:47 | +10 | ZEC | DOWN | 0.60 | open |  |
| 10-14 19:47 | +5 | ZEC | DOWN | 0.60 | open |  |
| 10-14 19:47 | +15 | BTC | DOWN | 0.64 | open |  |
| 10-14 19:47 | +10 stop | BTC | DOWN | 0.66 | open |  |
| 10-14 19:47 | +10 | BTC | DOWN | 0.66 | open |  |
| 10-14 19:46 | +5 | BTC | DOWN | 0.69 | open |  |
| 10-14 19:46 | +10 stop | XRP | DOWN | 0.65 | open |  |
| 10-14 19:46 | +20 | XRP | DOWN | 0.65 | open |  |
| 10-14 19:46 | +15 | XRP | DOWN | 0.65 | open |  |
| 10-14 19:46 | +10 | XRP | DOWN | 0.66 | open |  |
| 10-14 19:46 | +5 | XRP | DOWN | 0.66 | open |  |
| 10-14 19:46 | +10 stop | NEAR | DOWN | 0.60 | open |  |
| 10-14 19:46 | +20 | NEAR | DOWN | 0.60 | open |  |
| 10-14 19:46 | +15 | NEAR | DOWN | 0.60 | open |  |
| 10-14 19:46 | +10 | NEAR | DOWN | 0.60 | open |  |
| 10-14 19:46 | +5 | NEAR | DOWN | 0.60 | open |  |
| 10-14 19:46 | +10 stop | DOGE | DOWN | 0.70 | open |  |
| 10-14 19:46 | +20 | DOGE | DOWN | 0.70 | open |  |
| 10-14 19:46 | +15 | DOGE | DOWN | 0.70 | open |  |
| 10-14 19:46 | +10 | DOGE | DOWN | 0.70 | open |  |
| 10-14 19:46 | +5 | DOGE | DOWN | 0.70 | 0.76 | 0.32 |
| 10-14 19:46 | +10 stop | HYPE | UP | 0.56 | 0.67 | 0.76 |
| 10-14 19:46 | +20 | HYPE | UP | 0.56 | open |  |
| 10-14 19:46 | +15 | HYPE | UP | 0.56 | 0.75 | 1.58 |
| 10-14 19:46 | +10 | HYPE | UP | 0.56 | 0.67 | 0.76 |
| 10-14 19:46 | +5 | HYPE | UP | 0.56 | 0.67 | 0.76 |
| 10-14 19:46 | +10 stop | BNB | DOWN | 0.69 | open |  |
| 10-14 19:46 | +20 | BNB | DOWN | 0.69 | open |  |
| 10-14 19:46 | +15 | BNB | DOWN | 0.69 | open |  |
| 10-14 19:46 | +10 | BNB | DOWN | 0.69 | open |  |
| 10-14 19:46 | +5 | BNB | DOWN | 0.69 | open |  |
| 10-14 19:46 | +10 stop | ETH | DOWN | 0.65 | open |  |
| 10-14 19:46 | +20 | ETH | DOWN | 0.65 | open |  |
| 10-14 19:46 | +15 | ETH | DOWN | 0.65 | open |  |
| 10-14 19:46 | +10 | ETH | DOWN | 0.65 | open |  |
| 10-14 19:46 | +5 | ETH | DOWN | 0.65 | 0.71 | 0.29 |
| 10-14 19:46 | +10 stop | SOL | DOWN | 0.68 | open |  |
