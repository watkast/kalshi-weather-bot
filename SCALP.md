# Range-Scalp Bot

*Updated Tue Nov 03 14:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46049 | 40095 | 5954 (70) | 7 | $-13284.62 | -4.6% |
| **+10¢** | 34376 | 27478 | 6898 (92) | 7 | $-12153.08 | -5.6% |
| **+15¢** | 28770 | 21353 | 7417 (120) | 7 | $-11098.34 | -6.1% |
| **+20¢** | 25556 | 17783 | 7773 (157) | 7 | $-9861.49 | -6.2% |
| **+10¢ (15¢ stop)** | 56182 | 56093 | 89 (53) | 3 | $-21059.74 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 14:21 | +10 stop | SOL | UP | 0.60 | 0.74 | 1.09 |
| 11-03 14:20 | +10 stop | ZEC | UP | 0.59 | open |  |
| 11-03 14:20 | +10 stop | SOL | DOWN | 0.60 | 0.40 | -2.34 |
| 11-03 14:20 | +10 stop | DOGE | DOWN | 0.66 | 0.45 | -2.44 |
| 11-03 14:20 | +10 stop | BTC | DOWN | 0.62 | open |  |
| 11-03 14:19 | +10 stop | HYPE | DOWN | 0.61 | open |  |
| 11-03 14:19 | +10 stop | ZEC | UP | 0.68 | 0.53 | -1.84 |
| 11-03 14:19 | +10 stop | ETH | UP | 0.64 | 0.74 | 0.69 |
| 11-03 14:18 | +10 stop | XRP | DOWN | 0.58 | 0.78 | 1.69 |
| 11-03 14:18 | +20 | XRP | DOWN | 0.58 | 0.78 | 1.69 |
| 11-03 14:18 | +15 | XRP | DOWN | 0.58 | 0.78 | 1.69 |
| 11-03 14:18 | +10 | XRP | DOWN | 0.58 | 0.78 | 1.69 |
| 11-03 14:18 | +5 | XRP | DOWN | 0.58 | 0.67 | 0.56 |
| 11-03 14:18 | +10 stop | SOL | DOWN | 0.66 | 0.48 | -2.14 |
| 11-03 14:18 | +20 | SOL | DOWN | 0.66 | open |  |
| 11-03 14:18 | +15 | SOL | DOWN | 0.65 | open |  |
| 11-03 14:18 | +10 | SOL | DOWN | 0.67 | open |  |
| 11-03 14:18 | +5 | SOL | DOWN | 0.67 | open |  |
| 11-03 14:18 | +5 | BTC | DOWN | 0.60 | open |  |
| 11-03 14:18 | +5 | DOGE | DOWN | 0.62 | open |  |
| 11-03 14:17 | +10 stop | BNB | DOWN | 0.54 | 0.36 | -2.15 |
| 11-03 14:17 | +10 | BNB | DOWN | 0.54 | open |  |
| 11-03 14:17 | +5 | BNB | DOWN | 0.54 | open |  |
| 11-03 14:17 | +5 | BTC | DOWN | 0.60 | 0.65 | 0.17 |
| 11-03 14:16 | +10 stop | BTC | DOWN | 0.65 | 0.50 | -1.84 |
| 11-03 14:16 | +20 | BTC | DOWN | 0.65 | open |  |
| 11-03 14:16 | +15 | BTC | DOWN | 0.65 | open |  |
| 11-03 14:16 | +10 | BTC | DOWN | 0.65 | open |  |
| 11-03 14:16 | +5 | BTC | DOWN | 0.65 | 0.71 | 0.29 |
| 11-03 14:16 | +10 stop | BNB | DOWN | 0.60 | 0.73 | 0.99 |
| 11-03 14:16 | +20 | BNB | DOWN | 0.60 | open |  |
| 11-03 14:16 | +15 | BNB | DOWN | 0.60 | open |  |
| 11-03 14:16 | +10 | BNB | DOWN | 0.60 | 0.73 | 0.99 |
| 11-03 14:16 | +5 | BNB | DOWN | 0.60 | 0.73 | 0.99 |
| 11-03 14:16 | +10 stop | ZEC | DOWN | 0.70 | 0.51 | -2.23 |
| 11-03 14:16 | +20 | ZEC | DOWN | 0.70 | open |  |
| 11-03 14:16 | +15 | ZEC | DOWN | 0.70 | open |  |
| 11-03 14:16 | +10 | ZEC | DOWN | 0.70 | open |  |
| 11-03 14:16 | +5 | ZEC | DOWN | 0.70 | open |  |
| 11-03 14:16 | +10 stop | ETH | DOWN | 0.62 | 0.44 | -2.15 |
