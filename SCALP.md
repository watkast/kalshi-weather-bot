# Range-Scalp Bot

*Updated Sun Oct 18 08:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22315 | 19424 | 2891 (29) | 5 | $-6507.01 | -4.6% |
| **+10¢** | 16804 | 13465 | 3339 (42) | 6 | $-5784.54 | -5.5% |
| **+15¢** | 14071 | 10469 | 3602 (62) | 7 | $-5286.19 | -6.0% |
| **+20¢** | 12449 | 8676 | 3773 (80) | 8 | $-4737.70 | -6.1% |
| **+10¢ (15¢ stop)** | 27467 | 27417 | 50 (29) | 3 | $-10500.43 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 08:49 | +10 stop | NEAR | UP | 0.54 | 0.71 | 1.33 |
| 10-18 08:49 | +10 stop | DOGE | DOWN | 0.62 | 0.47 | -1.85 |
| 10-18 08:49 | +10 stop | SOL | DOWN | 0.67 | open |  |
| 10-18 08:49 | +10 | SOL | DOWN | 0.67 | open |  |
| 10-18 08:48 | +10 stop | BNB | DOWN | 0.60 | 0.45 | -1.85 |
| 10-18 08:48 | +5 | SOL | DOWN | 0.65 | open |  |
| 10-18 08:48 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-18 08:48 | +20 | ETH | DOWN | 0.71 | open |  |
| 10-18 08:48 | +15 | ETH | DOWN | 0.71 | 0.89 | 1.58 |
| 10-18 08:48 | +10 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-18 08:48 | +5 | ETH | DOWN | 0.71 | 0.80 | 0.63 |
| 10-18 08:48 | +10 stop | HYPE | DOWN | 0.63 | open |  |
| 10-18 08:48 | +20 | HYPE | DOWN | 0.63 | open |  |
| 10-18 08:48 | +15 | HYPE | DOWN | 0.63 | open |  |
| 10-18 08:48 | +10 | HYPE | DOWN | 0.63 | open |  |
| 10-18 08:48 | +5 | HYPE | DOWN | 0.63 | open |  |
| 10-18 08:47 | +10 stop | XRP | DOWN | 0.69 | 0.79 | 0.73 |
| 10-18 08:47 | +20 | XRP | DOWN | 0.69 | open |  |
| 10-18 08:47 | +15 | XRP | DOWN | 0.70 | open |  |
| 10-18 08:47 | +10 | XRP | DOWN | 0.69 | 0.79 | 0.73 |
| 10-18 08:47 | +5 | XRP | DOWN | 0.69 | 0.76 | 0.42 |
| 10-18 08:47 | +10 stop | BNB | UP | 0.58 | 0.41 | -2.09 |
| 10-18 08:47 | +10 stop | DOGE | UP | 0.54 | 0.38 | -1.95 |
| 10-18 08:47 | +20 | DOGE | UP | 0.54 | open |  |
| 10-18 08:47 | +15 | DOGE | UP | 0.53 | open |  |
| 10-18 08:47 | +10 | DOGE | UP | 0.53 | open |  |
| 10-18 08:47 | +5 | DOGE | UP | 0.53 | open |  |
| 10-18 08:47 | +10 stop | BTC | DOWN | 0.57 | 0.70 | 0.97 |
| 10-18 08:47 | +20 | BTC | DOWN | 0.57 | 0.80 | 2.00 |
| 10-18 08:47 | +15 | BTC | DOWN | 0.57 | 0.76 | 1.59 |
| 10-18 08:47 | +10 | BTC | DOWN | 0.57 | 0.70 | 0.97 |
| 10-18 08:47 | +5 | BTC | DOWN | 0.57 | 0.70 | 0.97 |
| 10-18 08:47 | +10 stop | SOL | DOWN | 0.52 | 0.66 | 1.06 |
| 10-18 08:47 | +10 | SOL | DOWN | 0.52 | 0.66 | 1.04 |
| 10-18 08:47 | +5 | SOL | DOWN | 0.57 | 0.66 | 0.56 |
| 10-18 08:47 | +10 stop | ZEC | DOWN | 0.70 | open |  |
| 10-18 08:47 | +20 | ZEC | DOWN | 0.70 | open |  |
| 10-18 08:47 | +15 | ZEC | DOWN | 0.70 | open |  |
| 10-18 08:47 | +10 | ZEC | DOWN | 0.67 | open |  |
| 10-18 08:47 | +5 | ZEC | DOWN | 0.67 | 0.73 | 0.30 |
