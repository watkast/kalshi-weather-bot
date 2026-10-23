# Range-Scalp Bot

*Updated Fri Oct 23 13:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30456 | 26535 | 3921 (39) | 1 | $-8837.70 | -4.6% |
| **+10¢** | 22799 | 18263 | 4536 (56) | 1 | $-7900.59 | -5.5% |
| **+15¢** | 19078 | 14199 | 4879 (79) | 1 | $-7126.13 | -5.9% |
| **+20¢** | 16892 | 11780 | 5112 (102) | 2 | $-6406.70 | -6.0% |
| **+10¢ (15¢ stop)** | 37325 | 37266 | 59 (32) | 0 | $-14101.02 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 13:59 | +10 stop | ZEC | DOWN | 0.10 | 0.68 | 5.57 |
| 10-23 13:58 | +10 stop | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
| 10-23 13:58 | +10 | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
| 10-23 13:58 | +5 | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
| 10-23 13:58 | +10 stop | HYPE | DOWN | 0.58 | 0.01 | -5.90 |
| 10-23 13:58 | +10 | HYPE | DOWN | 0.58 | open |  |
| 10-23 13:58 | +5 | HYPE | DOWN | 0.58 | open |  |
| 10-23 13:58 | +10 stop | XRP | UP | 0.56 | 0.67 | 0.76 |
| 10-23 13:58 | +15 | XRP | UP | 0.56 | 0.98 | 4.02 |
| 10-23 13:58 | +10 | XRP | UP | 0.54 | 0.67 | 0.96 |
| 10-23 13:58 | +5 | XRP | UP | 0.59 | 0.67 | 0.47 |
| 10-23 13:57 | +10 stop | SOL | DOWN | 0.49 | 0.65 | 1.26 |
| 10-23 13:55 | +10 stop | SOL | UP | 0.60 | 0.40 | -2.34 |
| 10-23 13:55 | +20 | SOL | UP | 0.61 | 0.82 | 1.83 |
| 10-23 13:55 | +15 | SOL | UP | 0.61 | 0.82 | 1.83 |
| 10-23 13:55 | +10 | SOL | UP | 0.61 | 0.82 | 1.83 |
| 10-23 13:55 | +5 | SOL | UP | 0.61 | 0.82 | 1.82 |
| 10-23 13:54 | +10 stop | BNB | DOWN | 0.50 | 0.64 | 1.05 |
| 10-23 13:54 | +20 | BNB | DOWN | 0.48 | 0.71 | 1.97 |
| 10-23 13:54 | +15 | BNB | DOWN | 0.48 | 0.64 | 1.25 |
| 10-23 13:54 | +10 | BNB | DOWN | 0.48 | 0.64 | 1.25 |
| 10-23 13:54 | +10 stop | BTC | DOWN | 0.69 | 0.88 | 1.67 |
| 10-23 13:54 | +10 | BTC | DOWN | 0.69 | 0.88 | 1.67 |
| 10-23 13:54 | +10 stop | XRP | DOWN | 0.53 | 0.64 | 0.75 |
| 10-23 13:54 | +15 | XRP | DOWN | 0.53 | 0.68 | 1.16 |
| 10-23 13:54 | +10 | XRP | DOWN | 0.53 | 0.64 | 0.75 |
| 10-23 13:54 | +10 stop | ETH | DOWN | 0.67 | 0.80 | 1.02 |
| 10-23 13:54 | +5 | ETH | DOWN | 0.67 | 0.80 | 1.02 |
| 10-23 13:54 | +10 stop | ZEC | UP | 0.58 | 0.21 | -4.00 |
| 10-23 13:54 | +20 | ZEC | UP | 0.59 | 0.82 | 2.02 |
| 10-23 13:54 | +15 | ZEC | UP | 0.59 | 0.82 | 2.02 |
| 10-23 13:54 | +10 | ZEC | UP | 0.59 | 0.82 | 2.02 |
| 10-23 13:54 | +5 | ZEC | UP | 0.62 | 0.82 | 1.76 |
| 10-23 13:53 | +10 stop | XRP | UP | 0.54 | 0.68 | 1.06 |
| 10-23 13:52 | +5 | BNB | DOWN | 0.64 | 0.71 | 0.38 |
| 10-23 13:52 | +5 | ETH | DOWN | 0.57 | 0.71 | 1.07 |
| 10-23 13:52 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-23 13:52 | +10 stop | ETH | DOWN | 0.60 | 0.71 | 0.78 |
| 10-23 13:52 | +5 | ETH | DOWN | 0.58 | 0.64 | 0.25 |
| 10-23 13:52 | +5 | SOL | UP | 0.66 | 0.76 | 0.71 |
