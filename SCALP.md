# Range-Scalp Bot

*Updated Wed Oct 28 14:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38197 | 33328 | 4869 (46) | 6 | $-10768.06 | -4.5% |
| **+10¢** | 28489 | 22859 | 5630 (68) | 7 | $-9603.61 | -5.4% |
| **+15¢** | 23836 | 17792 | 6044 (93) | 7 | $-8543.79 | -5.7% |
| **+20¢** | 21144 | 14814 | 6330 (118) | 7 | $-7509.88 | -5.7% |
| **+10¢ (15¢ stop)** | 46755 | 46688 | 67 (35) | 2 | $-17763.02 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 14:05 | +10 stop | SOL | UP | 0.64 | open |  |
| 10-28 14:04 | +10 stop | NEAR | UP | 0.71 | open |  |
| 10-28 14:04 | +5 | NEAR | UP | 0.71 | open |  |
| 10-28 14:04 | +5 | SOL | UP | 0.66 | open |  |
| 10-28 14:04 | +5 | ETH | UP | 0.63 | 0.74 | 0.79 |
| 10-28 14:04 | +5 | DOGE | UP | 0.66 | 0.77 | 0.81 |
| 10-28 14:03 | +10 stop | ETH | UP | 0.61 | 0.74 | 0.99 |
| 10-28 14:03 | +10 stop | BTC | UP | 0.58 | 0.72 | 1.07 |
| 10-28 14:03 | +5 | ETH | UP | 0.59 | 0.64 | 0.16 |
| 10-28 14:03 | +10 stop | DOGE | UP | 0.55 | 0.69 | 1.07 |
| 10-28 14:03 | +20 | DOGE | UP | 0.56 | 0.77 | 1.80 |
| 10-28 14:03 | +15 | DOGE | UP | 0.55 | 0.70 | 1.17 |
| 10-28 14:03 | +10 | DOGE | UP | 0.55 | 0.69 | 1.07 |
| 10-28 14:03 | +5 | DOGE | UP | 0.57 | 0.63 | 0.28 |
| 10-28 14:03 | +10 stop | BNB | UP | 0.59 | 0.76 | 1.40 |
| 10-28 14:03 | +5 | NEAR | UP | 0.53 | 0.61 | 0.45 |
| 10-28 14:03 | +10 stop | HYPE | UP | 0.63 | 0.75 | 0.89 |
| 10-28 14:03 | +20 | HYPE | UP | 0.63 | 0.83 | 1.73 |
| 10-28 14:03 | +15 | HYPE | UP | 0.63 | 0.82 | 1.62 |
| 10-28 14:03 | +10 | HYPE | UP | 0.63 | 0.75 | 0.89 |
| 10-28 14:03 | +5 | HYPE | UP | 0.63 | 0.69 | 0.28 |
| 10-28 14:02 | +10 stop | ZEC | UP | 0.64 | 0.74 | 0.74 |
| 10-28 14:02 | +10 stop | SOL | DOWN | 0.57 | 0.42 | -1.86 |
| 10-28 14:02 | +20 | SOL | DOWN | 0.57 | open |  |
| 10-28 14:02 | +15 | SOL | DOWN | 0.58 | open |  |
| 10-28 14:02 | +10 | SOL | DOWN | 0.58 | open |  |
| 10-28 14:02 | +5 | SOL | DOWN | 0.58 | 0.64 | 0.25 |
| 10-28 14:02 | +5 | ETH | DOWN | 0.48 | 0.56 | 0.44 |
| 10-28 14:02 | +5 | NEAR | DOWN | 0.52 | 0.58 | 0.24 |
| 10-28 14:02 | +10 stop | XRP | DOWN | 0.53 | 0.37 | -1.95 |
| 10-28 14:02 | +20 | XRP | DOWN | 0.53 | open |  |
| 10-28 14:02 | +15 | XRP | DOWN | 0.53 | open |  |
| 10-28 14:02 | +10 | XRP | DOWN | 0.53 | open |  |
| 10-28 14:02 | +5 | XRP | DOWN | 0.53 | open |  |
| 10-28 14:01 | +10 stop | NEAR | DOWN | 0.54 | 0.36 | -2.15 |
| 10-28 14:01 | +20 | NEAR | DOWN | 0.54 | open |  |
| 10-28 14:01 | +15 | NEAR | DOWN | 0.54 | open |  |
| 10-28 14:01 | +10 | NEAR | DOWN | 0.54 | open |  |
| 10-28 14:01 | +5 | NEAR | DOWN | 0.54 | 0.62 | 0.45 |
| 10-28 14:01 | +10 stop | ETH | DOWN | 0.59 | 0.44 | -1.85 |
