# Range-Scalp Bot

*Updated Wed Nov 04 09:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47004 | 40932 | 6072 (72) | 4 | $-13530.46 | -4.6% |
| **+10¢** | 35115 | 28075 | 7040 (96) | 4 | $-12343.39 | -5.6% |
| **+15¢** | 29406 | 21829 | 7577 (124) | 4 | $-11298.80 | -6.1% |
| **+20¢** | 26124 | 18188 | 7936 (164) | 5 | $-9953.36 | -6.1% |
| **+10¢ (15¢ stop)** | 57286 | 57193 | 93 (56) | 3 | $-21346.91 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 09:02 | +10 stop | XRP | DOWN | 0.68 | open |  |
| 11-04 09:02 | +10 stop | BTC | DOWN | 0.70 | open |  |
| 11-04 09:01 | +10 stop | HYPE | DOWN | 0.67 | open |  |
| 11-04 09:01 | +20 | HYPE | DOWN | 0.67 | open |  |
| 11-04 09:01 | +15 | HYPE | DOWN | 0.67 | open |  |
| 11-04 09:01 | +10 | HYPE | DOWN | 0.67 | open |  |
| 11-04 09:01 | +5 | HYPE | DOWN | 0.67 | open |  |
| 11-04 09:01 | +10 stop | DOGE | DOWN | 0.69 | 0.83 | 1.15 |
| 11-04 09:01 | +20 | DOGE | DOWN | 0.69 | open |  |
| 11-04 09:01 | +15 | DOGE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-04 09:01 | +10 | DOGE | DOWN | 0.69 | 0.83 | 1.15 |
| 11-04 09:01 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
| 11-04 09:00 | +10 stop | XRP | UP | 0.64 | 0.48 | -1.95 |
| 11-04 09:00 | +20 | XRP | UP | 0.64 | open |  |
| 11-04 09:00 | +15 | XRP | UP | 0.64 | open |  |
| 11-04 09:00 | +10 | XRP | UP | 0.64 | open |  |
| 11-04 09:00 | +5 | XRP | UP | 0.64 | open |  |
| 11-04 09:00 | +10 stop | ETH | UP | 0.56 | 0.41 | -1.85 |
| 11-04 09:00 | +20 | ETH | UP | 0.56 | open |  |
| 11-04 09:00 | +15 | ETH | UP | 0.56 | open |  |
| 11-04 09:00 | +10 | ETH | UP | 0.56 | open |  |
| 11-04 09:00 | +5 | ETH | UP | 0.56 | open |  |
| 11-04 09:00 | +10 stop | NEAR | DOWN | 0.66 | 0.81 | 1.23 |
| 11-04 09:00 | +20 | NEAR | DOWN | 0.66 | 0.88 | 1.96 |
| 11-04 09:00 | +15 | NEAR | DOWN | 0.66 | 0.81 | 1.23 |
| 11-04 09:00 | +10 | NEAR | DOWN | 0.66 | 0.81 | 1.23 |
| 11-04 09:00 | +5 | NEAR | DOWN | 0.66 | 0.71 | 0.19 |
| 11-04 09:00 | +10 stop | BTC | UP | 0.60 | 0.44 | -1.95 |
| 11-04 09:00 | +20 | BTC | UP | 0.60 | open |  |
| 11-04 09:00 | +15 | BTC | UP | 0.60 | open |  |
| 11-04 09:00 | +10 | BTC | UP | 0.60 | open |  |
| 11-04 09:00 | +5 | BTC | UP | 0.60 | open |  |
| 11-04 08:57 | +10 stop | BNB | UP | 0.40 | 0.52 | 0.85 |
| 11-04 08:57 | +10 stop | XRP | UP | 0.41 | 0.66 | 2.17 |
| 11-04 08:57 | +20 | XRP | UP | 0.41 | 0.66 | 2.17 |
| 11-04 08:57 | +10 | XRP | UP | 0.41 | 0.66 | 2.17 |
| 11-04 08:57 | +5 | XRP | UP | 0.42 | 0.66 | 2.06 |
| 11-04 08:56 | +10 stop | SOL | UP | 0.49 | 0.09 | -4.25 |
| 11-04 08:56 | +10 stop | NEAR | DOWN | 0.67 | 0.77 | 0.73 |
| 11-04 08:56 | +15 | NEAR | DOWN | 0.67 | 0.86 | 1.67 |
