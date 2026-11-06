# Range-Scalp Bot

*Updated Fri Nov 06 06:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49287 | 42945 | 6342 (75) | 3 | $-13988.25 | -4.5% |
| **+10¢** | 36800 | 29430 | 7370 (101) | 4 | $-12829.27 | -5.5% |
| **+15¢** | 30824 | 22888 | 7936 (130) | 5 | $-11711.72 | -6.1% |
| **+20¢** | 27398 | 19080 | 8318 (170) | 8 | $-10363.45 | -6.0% |
| **+10¢ (15¢ stop)** | 60095 | 60000 | 95 (57) | 3 | $-22260.01 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 06:05 | +10 stop | NEAR | DOWN | 0.70 | open |  |
| 11-06 06:05 | +20 | NEAR | DOWN | 0.70 | open |  |
| 11-06 06:05 | +15 | NEAR | DOWN | 0.70 | open |  |
| 11-06 06:05 | +10 | NEAR | DOWN | 0.70 | open |  |
| 11-06 06:05 | +5 | NEAR | DOWN | 0.70 | 0.75 | 0.21 |
| 11-06 06:05 | +10 stop | BNB | DOWN | 0.69 | open |  |
| 11-06 06:05 | +20 | BNB | DOWN | 0.69 | open |  |
| 11-06 06:05 | +15 | BNB | DOWN | 0.69 | open |  |
| 11-06 06:05 | +10 | BNB | DOWN | 0.69 | open |  |
| 11-06 06:05 | +5 | BNB | DOWN | 0.67 | open |  |
| 11-06 06:04 | +5 | ZEC | DOWN | 0.70 | open |  |
| 11-06 06:03 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-06 06:03 | +20 | ETH | DOWN | 0.68 | open |  |
| 11-06 06:03 | +15 | ETH | DOWN | 0.68 | open |  |
| 11-06 06:03 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-06 06:03 | +5 | ETH | DOWN | 0.68 | 0.76 | 0.51 |
| 11-06 06:03 | +10 stop | ZEC | DOWN | 0.57 | 0.72 | 1.17 |
| 11-06 06:03 | +20 | ZEC | DOWN | 0.57 | open |  |
| 11-06 06:03 | +15 | ZEC | DOWN | 0.57 | 0.72 | 1.17 |
| 11-06 06:03 | +10 | ZEC | DOWN | 0.57 | 0.72 | 1.17 |
| 11-06 06:03 | +5 | ZEC | DOWN | 0.57 | 0.62 | 0.15 |
| 11-06 06:03 | +10 stop | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-06 06:03 | +20 | SOL | DOWN | 0.63 | open |  |
| 11-06 06:03 | +15 | SOL | DOWN | 0.63 | 0.80 | 1.41 |
| 11-06 06:03 | +10 | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 11-06 06:03 | +5 | SOL | DOWN | 0.63 | 0.71 | 0.48 |
| 11-06 06:03 | +10 stop | BTC | DOWN | 0.68 | open |  |
| 11-06 06:03 | +10 | BTC | DOWN | 0.68 | open |  |
| 11-06 06:03 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-06 06:01 | +10 stop | HYPE | DOWN | 0.70 | 0.52 | -2.13 |
| 11-06 06:01 | +20 | HYPE | DOWN | 0.70 | open |  |
| 11-06 06:01 | +15 | HYPE | DOWN | 0.70 | open |  |
| 11-06 06:01 | +10 | HYPE | DOWN | 0.70 | open |  |
| 11-06 06:01 | +5 | HYPE | DOWN | 0.70 | open |  |
| 11-06 06:01 | +10 stop | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-06 06:01 | +20 | DOGE | DOWN | 0.68 | open |  |
| 11-06 06:01 | +15 | DOGE | DOWN | 0.68 | 0.85 | 1.45 |
| 11-06 06:01 | +10 | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-06 06:01 | +5 | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-06 06:00 | +10 stop | XRP | DOWN | 0.69 | 0.79 | 0.73 |
