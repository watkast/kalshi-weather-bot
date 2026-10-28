# Range-Scalp Bot

*Updated Wed Oct 28 12:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38102 | 33242 | 4860 (46) | 2 | $-10757.90 | -4.5% |
| **+10¢** | 28424 | 22804 | 5620 (68) | 2 | $-9600.04 | -5.4% |
| **+15¢** | 23779 | 17745 | 6034 (93) | 4 | $-8554.73 | -5.7% |
| **+20¢** | 21087 | 14768 | 6319 (118) | 8 | $-7533.87 | -5.7% |
| **+10¢ (15¢ stop)** | 46645 | 46578 | 67 (35) | 2 | $-17741.36 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 12:33 | +5 | ETH | DOWN | 0.67 | open |  |
| 10-28 12:32 | +5 | ZEC | DOWN | 0.67 | 0.72 | 0.19 |
| 10-28 12:32 | +5 | NEAR | UP | 0.61 | open |  |
| 10-28 12:32 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.42 |
| 10-28 12:31 | +10 stop | NEAR | UP | 0.57 | open |  |
| 10-28 12:31 | +20 | NEAR | UP | 0.57 | open |  |
| 10-28 12:31 | +15 | NEAR | UP | 0.57 | open |  |
| 10-28 12:31 | +10 | NEAR | UP | 0.57 | open |  |
| 10-28 12:31 | +5 | NEAR | UP | 0.57 | 0.65 | 0.46 |
| 10-28 12:31 | +10 stop | ETH | DOWN | 0.61 | open |  |
| 10-28 12:31 | +20 | ETH | DOWN | 0.61 | open |  |
| 10-28 12:31 | +15 | ETH | DOWN | 0.61 | open |  |
| 10-28 12:31 | +10 | ETH | DOWN | 0.61 | open |  |
| 10-28 12:31 | +5 | ETH | DOWN | 0.61 | 0.67 | 0.27 |
| 10-28 12:31 | +10 stop | ZEC | DOWN | 0.60 | 0.72 | 0.88 |
| 10-28 12:31 | +20 | ZEC | DOWN | 0.60 | open |  |
| 10-28 12:31 | +15 | ZEC | DOWN | 0.60 | 0.75 | 1.19 |
| 10-28 12:31 | +10 | ZEC | DOWN | 0.60 | 0.72 | 0.88 |
| 10-28 12:31 | +5 | ZEC | DOWN | 0.60 | 0.67 | 0.37 |
| 10-28 12:31 | +10 stop | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 10-28 12:31 | +20 | BNB | DOWN | 0.66 | open |  |
| 10-28 12:31 | +15 | BNB | DOWN | 0.66 | 0.81 | 1.23 |
| 10-28 12:31 | +10 | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 10-28 12:31 | +5 | BNB | DOWN | 0.66 | 0.73 | 0.40 |
| 10-28 12:31 | +10 stop | HYPE | DOWN | 0.59 | 0.81 | 1.92 |
| 10-28 12:31 | +20 | HYPE | DOWN | 0.59 | 0.81 | 1.92 |
| 10-28 12:31 | +15 | HYPE | DOWN | 0.59 | 0.81 | 1.92 |
| 10-28 12:31 | +10 | HYPE | DOWN | 0.59 | 0.81 | 1.92 |
| 10-28 12:31 | +5 | HYPE | DOWN | 0.59 | 0.81 | 1.92 |
| 10-28 12:31 | +10 stop | SOL | DOWN | 0.59 | 0.73 | 1.09 |
| 10-28 12:31 | +20 | SOL | DOWN | 0.59 | open |  |
| 10-28 12:31 | +15 | SOL | DOWN | 0.59 | 0.75 | 1.29 |
| 10-28 12:31 | +10 | SOL | DOWN | 0.59 | 0.73 | 1.09 |
| 10-28 12:31 | +5 | SOL | DOWN | 0.59 | 0.66 | 0.37 |
| 10-28 12:31 | +10 stop | DOGE | DOWN | 0.59 | 0.71 | 0.88 |
| 10-28 12:31 | +20 | DOGE | DOWN | 0.59 | open |  |
| 10-28 12:31 | +15 | DOGE | DOWN | 0.59 | 0.75 | 1.29 |
| 10-28 12:31 | +10 | DOGE | DOWN | 0.59 | 0.71 | 0.88 |
| 10-28 12:31 | +5 | DOGE | DOWN | 0.60 | 0.65 | 0.17 |
| 10-28 12:31 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
