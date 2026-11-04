# Range-Scalp Bot

*Updated Wed Nov 04 07:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46877 | 40829 | 6048 (72) | 4 | $-13427.96 | -4.5% |
| **+10¢** | 35021 | 28009 | 7012 (96) | 4 | $-12238.21 | -5.6% |
| **+15¢** | 29323 | 21777 | 7546 (124) | 4 | $-11184.06 | -6.1% |
| **+20¢** | 26049 | 18146 | 7903 (164) | 5 | $-9830.50 | -6.0% |
| **+10¢ (15¢ stop)** | 57141 | 57048 | 93 (56) | 4 | $-21302.94 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 07:10 | +10 stop | BTC | UP | 0.57 | open |  |
| 11-04 07:10 | +20 | BTC | UP | 0.57 | open |  |
| 11-04 07:10 | +15 | BTC | UP | 0.57 | open |  |
| 11-04 07:10 | +10 | BTC | UP | 0.57 | open |  |
| 11-04 07:10 | +5 | BTC | UP | 0.57 | open |  |
| 11-04 07:10 | +10 stop | SOL | DOWN | 0.61 | open |  |
| 11-04 07:10 | +20 | SOL | DOWN | 0.61 | open |  |
| 11-04 07:10 | +15 | SOL | DOWN | 0.61 | open |  |
| 11-04 07:10 | +10 | SOL | DOWN | 0.61 | open |  |
| 11-04 07:10 | +5 | SOL | DOWN | 0.61 | open |  |
| 11-04 07:10 | +10 stop | HYPE | UP | 0.67 | open |  |
| 11-04 07:10 | +15 | HYPE | UP | 0.69 | open |  |
| 11-04 07:10 | +10 | HYPE | UP | 0.70 | open |  |
| 11-04 07:10 | +5 | HYPE | UP | 0.70 | open |  |
| 11-04 07:10 | +10 stop | BNB | DOWN | 0.58 | open |  |
| 11-04 07:07 | +10 stop | NEAR | DOWN | 0.66 | 0.79 | 1.02 |
| 11-04 07:07 | +20 | NEAR | DOWN | 0.66 | open |  |
| 11-04 07:07 | +15 | NEAR | DOWN | 0.66 | 0.84 | 1.54 |
| 11-04 07:07 | +10 | NEAR | DOWN | 0.66 | 0.79 | 1.02 |
| 11-04 07:07 | +5 | NEAR | DOWN | 0.66 | 0.74 | 0.50 |
| 11-04 07:07 | +5 | ZEC | DOWN | 0.65 | 0.72 | 0.39 |
| 11-04 07:07 | +10 stop | HYPE | DOWN | 0.68 | 0.83 | 1.28 |
| 11-04 07:07 | +20 | HYPE | DOWN | 0.68 | open |  |
| 11-04 07:07 | +15 | HYPE | DOWN | 0.68 | 0.83 | 1.28 |
| 11-04 07:07 | +10 | HYPE | DOWN | 0.68 | 0.83 | 1.28 |
| 11-04 07:07 | +5 | HYPE | DOWN | 0.68 | 0.75 | 0.44 |
| 11-04 07:06 | +10 stop | ETH | DOWN | 0.62 | 0.77 | 1.20 |
| 11-04 07:06 | +10 stop | ZEC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-04 07:06 | +15 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 11-04 07:06 | +10 | ZEC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-04 07:06 | +5 | ZEC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-04 07:04 | +10 stop | BNB | DOWN | 0.62 | 0.77 | 1.20 |
| 11-04 07:03 | +10 stop | ETH | DOWN | 0.67 | 0.79 | 0.92 |
| 11-04 07:02 | +5 | NEAR | DOWN | 0.69 | 0.76 | 0.42 |
| 11-04 07:02 | +5 | BTC | DOWN | 0.57 | 0.64 | 0.35 |
| 11-04 07:02 | +10 stop | BNB | UP | 0.59 | 0.34 | -2.83 |
| 11-04 07:02 | +10 | BNB | UP | 0.59 | open |  |
| 11-04 07:02 | +10 stop | ETH | UP | 0.59 | 0.40 | -2.24 |
| 11-04 07:02 | +10 | ETH | UP | 0.59 | 0.75 | 1.29 |
| 11-04 07:02 | +5 | ETH | UP | 0.59 | 0.68 | 0.57 |
