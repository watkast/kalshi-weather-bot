# Range-Scalp Bot

*Updated Thu Oct 15 10:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17328 | 15045 | 2283 (28) | 2 | $-5256.54 | -4.8% |
| **+10¢** | 13095 | 10448 | 2647 (40) | 1 | $-4785.71 | -5.8% |
| **+15¢** | 10999 | 8156 | 2843 (59) | 1 | $-4249.08 | -6.2% |
| **+20¢** | 9771 | 6797 | 2974 (77) | 1 | $-3684.79 | -6.0% |
| **+10¢ (15¢ stop)** | 21305 | 21255 | 50 (29) | 0 | $-8227.46 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 10:05 | +15 | HYPE | DOWN | 0.69 | 0.85 | 1.32 |
| 10-15 10:05 | +10 | HYPE | DOWN | 0.69 | 0.80 | 0.79 |
| 10-15 10:05 | +10 stop | HYPE | DOWN | 0.70 | 0.83 | 1.01 |
| 10-15 10:05 | +20 | HYPE | DOWN | 0.70 | 0.92 | 1.91 |
| 10-15 10:05 | +10 stop | NEAR | DOWN | 0.62 | 0.76 | 1.10 |
| 10-15 10:05 | +5 | NEAR | DOWN | 0.62 | 0.68 | 0.27 |
| 10-15 10:05 | +10 stop | ETH | DOWN | 0.62 | 0.72 | 0.68 |
| 10-15 10:05 | +20 | ETH | DOWN | 0.62 | 0.84 | 1.93 |
| 10-15 10:05 | +15 | ETH | DOWN | 0.62 | 0.77 | 1.20 |
| 10-15 10:05 | +10 | ETH | DOWN | 0.62 | 0.72 | 0.68 |
| 10-15 10:05 | +5 | ETH | DOWN | 0.62 | 0.67 | 0.17 |
| 10-15 10:05 | +10 stop | BTC | DOWN | 0.63 | 0.76 | 1.00 |
| 10-15 10:04 | +10 stop | ETH | UP | 0.37 | 0.55 | 1.45 |
| 10-15 10:04 | +10 | ETH | UP | 0.37 | 0.55 | 1.45 |
| 10-15 10:04 | +5 | ETH | UP | 0.37 | 0.55 | 1.45 |
| 10-15 10:03 | +10 stop | ETH | DOWN | 0.49 | 0.63 | 1.05 |
| 10-15 10:03 | +20 | ETH | DOWN | 0.49 | 0.72 | 1.97 |
| 10-15 10:03 | +15 | ETH | DOWN | 0.49 | 0.64 | 1.15 |
| 10-15 10:03 | +10 | ETH | DOWN | 0.49 | 0.63 | 1.05 |
| 10-15 10:03 | +5 | ETH | DOWN | 0.49 | 0.63 | 1.05 |
| 10-15 10:03 | +5 | DOGE | DOWN | 0.70 | 0.78 | 0.50 |
| 10-15 10:03 | +5 | SOL | DOWN | 0.53 | 0.70 | 1.37 |
| 10-15 10:02 | +10 stop | BNB | DOWN | 0.61 | 0.73 | 0.89 |
| 10-15 10:02 | +20 | BNB | DOWN | 0.61 | 0.81 | 1.72 |
| 10-15 10:02 | +15 | BNB | DOWN | 0.61 | 0.81 | 1.72 |
| 10-15 10:02 | +10 | BNB | DOWN | 0.61 | 0.73 | 0.89 |
| 10-15 10:02 | +5 | BNB | DOWN | 0.61 | 0.73 | 0.89 |
| 10-15 10:02 | +5 | HYPE | UP | 0.61 | open |  |
| 10-15 10:02 | +10 stop | BTC | UP | 0.53 | 0.35 | -2.14 |
| 10-15 10:02 | +20 | BTC | UP | 0.53 | open |  |
| 10-15 10:02 | +15 | BTC | UP | 0.53 | open |  |
| 10-15 10:02 | +10 | BTC | UP | 0.53 | open |  |
| 10-15 10:02 | +5 | BTC | UP | 0.53 | open |  |
| 10-15 10:01 | +10 stop | NEAR | DOWN | 0.66 | 0.47 | -2.24 |
| 10-15 10:01 | +20 | NEAR | DOWN | 0.66 | 0.88 | 1.96 |
| 10-15 10:01 | +15 | NEAR | DOWN | 0.66 | 0.84 | 1.54 |
| 10-15 10:01 | +10 | NEAR | DOWN | 0.66 | 0.76 | 0.71 |
| 10-15 10:01 | +5 | NEAR | DOWN | 0.66 | 0.73 | 0.40 |
| 10-15 10:01 | +10 stop | SOL | DOWN | 0.50 | 0.70 | 1.67 |
| 10-15 10:01 | +20 | SOL | DOWN | 0.50 | 0.70 | 1.67 |
