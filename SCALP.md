# Range-Scalp Bot

*Updated Sun Nov 22 01:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68071 | 59409 | 8662 (138) | 2 | $-18250.56 | -4.3% |
| **+10¢** | 50820 | 40703 | 10117 (181) | 4 | $-16912.37 | -5.3% |
| **+15¢** | 42599 | 31691 | 10908 (230) | 5 | $-15183.61 | -5.7% |
| **+20¢** | 37921 | 26457 | 11464 (288) | 8 | $-13508.53 | -5.7% |
| **+10¢ (15¢ stop)** | 82862 | 82684 | 178 (110) | 2 | $-30414.46 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 01:18 | +5 | SOL | DOWN | 0.65 | 0.70 | 0.19 |
| 11-22 01:17 | +5 | SOL | DOWN | 0.58 | 0.66 | 0.46 |
| 11-22 01:17 | +5 | DOGE | DOWN | 0.63 | 0.71 | 0.48 |
| 11-22 01:17 | +10 stop | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-22 01:17 | +10 | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-22 01:17 | +5 | ZEC | DOWN | 0.67 | 0.72 | 0.19 |
| 11-22 01:17 | +5 | ETH | DOWN | 0.56 | open |  |
| 11-22 01:16 | +20 | BNB | DOWN | 0.71 | open |  |
| 11-22 01:16 | +15 | BNB | DOWN | 0.71 | open |  |
| 11-22 01:16 | +10 | BNB | DOWN | 0.71 | open |  |
| 11-22 01:16 | +5 | BNB | DOWN | 0.70 | 0.77 | 0.42 |
| 11-22 01:16 | +10 stop | BTC | DOWN | 0.56 | open |  |
| 11-22 01:16 | +20 | BTC | DOWN | 0.57 | open |  |
| 11-22 01:16 | +15 | BTC | DOWN | 0.57 | open |  |
| 11-22 01:16 | +10 | BTC | DOWN | 0.57 | open |  |
| 11-22 01:16 | +5 | BTC | DOWN | 0.57 | open |  |
| 11-22 01:16 | +10 stop | NEAR | DOWN | 0.67 | 0.50 | -2.04 |
| 11-22 01:16 | +20 | NEAR | DOWN | 0.67 | open |  |
| 11-22 01:16 | +15 | NEAR | DOWN | 0.67 | open |  |
| 11-22 01:16 | +10 | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-22 01:16 | +5 | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-22 01:16 | +5 | ETH | DOWN | 0.50 | 0.59 | 0.55 |
| 11-22 01:16 | +10 stop | XRP | DOWN | 0.60 | 0.74 | 1.09 |
| 11-22 01:16 | +20 | XRP | DOWN | 0.55 | 0.75 | 1.68 |
| 11-22 01:16 | +15 | XRP | DOWN | 0.55 | 0.74 | 1.58 |
| 11-22 01:16 | +10 | XRP | DOWN | 0.55 | 0.67 | 0.86 |
| 11-22 01:16 | +5 | XRP | DOWN | 0.55 | 0.60 | 0.15 |
| 11-22 01:15 | +10 stop | ETH | DOWN | 0.58 | 0.43 | -1.86 |
| 11-22 01:15 | +20 | ETH | DOWN | 0.58 | open |  |
| 11-22 01:15 | +15 | ETH | DOWN | 0.58 | open |  |
| 11-22 01:15 | +10 | ETH | DOWN | 0.58 | open |  |
| 11-22 01:15 | +5 | ETH | DOWN | 0.57 | 0.62 | 0.15 |
| 11-22 01:15 | +10 stop | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-22 01:15 | +20 | ZEC | DOWN | 0.60 | open |  |
| 11-22 01:15 | +15 | ZEC | DOWN | 0.60 | 0.77 | 1.40 |
| 11-22 01:15 | +10 | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-22 01:15 | +5 | ZEC | DOWN | 0.60 | 0.66 | 0.27 |
| 11-22 01:15 | +10 stop | HYPE | DOWN | 0.61 | 0.73 | 0.89 |
| 11-22 01:15 | +20 | HYPE | DOWN | 0.61 | open |  |
| 11-22 01:15 | +15 | HYPE | DOWN | 0.61 | 0.76 | 1.20 |
