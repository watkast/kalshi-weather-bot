# Range-Scalp Bot

*Updated Wed Nov 04 12:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47228 | 41129 | 6099 (72) | 2 | $-13580.89 | -4.6% |
| **+10¢** | 35277 | 28200 | 7077 (97) | 2 | $-12423.64 | -5.6% |
| **+15¢** | 29541 | 21921 | 7620 (125) | 2 | $-11391.89 | -6.1% |
| **+20¢** | 26244 | 18263 | 7981 (165) | 2 | $-10051.80 | -6.1% |
| **+10¢ (15¢ stop)** | 57562 | 57469 | 93 (56) | 0 | $-21469.08 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 12:02 | +10 stop | BTC | DOWN | 0.65 | 0.78 | 1.01 |
| 11-04 12:02 | +10 stop | ETH | DOWN | 0.62 | 0.75 | 1.00 |
| 11-04 12:02 | +20 | ETH | DOWN | 0.61 | 0.83 | 1.93 |
| 11-04 12:02 | +15 | ETH | DOWN | 0.62 | 0.79 | 1.41 |
| 11-04 12:02 | +10 | ETH | DOWN | 0.62 | 0.75 | 0.99 |
| 11-04 12:02 | +5 | ETH | DOWN | 0.62 | 0.67 | 0.17 |
| 11-04 12:02 | +10 stop | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 11-04 12:02 | +20 | BNB | DOWN | 0.71 | 0.91 | 1.80 |
| 11-04 12:02 | +15 | BNB | DOWN | 0.71 | 0.88 | 1.47 |
| 11-04 12:02 | +10 | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 11-04 12:02 | +5 | BNB | DOWN | 0.71 | 0.80 | 0.63 |
| 11-04 12:01 | +10 stop | NEAR | DOWN | 0.70 | 0.82 | 0.94 |
| 11-04 12:01 | +20 | NEAR | DOWN | 0.70 | 0.91 | 1.87 |
| 11-04 12:01 | +15 | NEAR | DOWN | 0.69 | 0.89 | 1.78 |
| 11-04 12:01 | +10 | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 11-04 12:01 | +5 | NEAR | DOWN | 0.69 | 0.77 | 0.52 |
| 11-04 12:01 | +10 stop | ETH | UP | 0.37 | 0.61 | 2.06 |
| 11-04 12:01 | +20 | ETH | UP | 0.41 | 0.61 | 1.66 |
| 11-04 12:01 | +15 | ETH | UP | 0.41 | 0.61 | 1.66 |
| 11-04 12:01 | +10 | ETH | UP | 0.41 | 0.61 | 1.66 |
| 11-04 12:01 | +5 | ETH | UP | 0.41 | 0.61 | 1.66 |
| 11-04 12:00 | +10 stop | BTC | UP | 0.59 | 0.42 | -2.05 |
| 11-04 12:00 | +20 | BTC | UP | 0.59 | open |  |
| 11-04 12:00 | +15 | BTC | UP | 0.59 | open |  |
| 11-04 12:00 | +10 | BTC | UP | 0.59 | open |  |
| 11-04 12:00 | +5 | BTC | UP | 0.59 | open |  |
| 11-04 12:00 | +10 stop | DOGE | UP | 0.60 | 0.27 | -3.61 |
| 11-04 12:00 | +20 | DOGE | UP | 0.60 | open |  |
| 11-04 12:00 | +15 | DOGE | UP | 0.60 | open |  |
| 11-04 12:00 | +10 | DOGE | UP | 0.60 | open |  |
| 11-04 12:00 | +5 | DOGE | UP | 0.59 | open |  |
| 11-04 11:53 | +10 stop | BNB | DOWN | 0.66 | 0.81 | 1.23 |
| 11-04 11:52 | +10 stop | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-04 11:52 | +5 | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 11-04 11:52 | +10 stop | BNB | UP | 0.58 | 0.30 | -3.17 |
| 11-04 11:52 | +5 | ETH | DOWN | 0.71 | 0.77 | 0.32 |
| 11-04 11:52 | +10 stop | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-04 11:52 | +5 | HYPE | DOWN | 0.70 | 0.75 | 0.21 |
| 11-04 11:51 | +10 stop | BTC | DOWN | 0.59 | 0.69 | 0.68 |
| 11-04 11:50 | +10 stop | BTC | DOWN | 0.59 | 0.69 | 0.68 |
