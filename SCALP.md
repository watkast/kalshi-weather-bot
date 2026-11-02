# Range-Scalp Bot

*Updated Mon Nov 02 13:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44940 | 39133 | 5807 (66) | 4 | $-12989.82 | -4.6% |
| **+10¢** | 33551 | 26821 | 6730 (87) | 5 | $-11864.89 | -5.6% |
| **+15¢** | 28058 | 20815 | 7243 (114) | 6 | $-10934.78 | -6.2% |
| **+20¢** | 24927 | 17344 | 7583 (149) | 6 | $-9667.48 | -6.2% |
| **+10¢ (15¢ stop)** | 54853 | 54766 | 87 (51) | 0 | $-20743.44 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 13:51 | +10 stop | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 11-02 13:51 | +5 | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 11-02 13:48 | +10 stop | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-02 13:48 | +10 stop | SOL | DOWN | 0.69 | 0.80 | 0.83 |
| 11-02 13:48 | +10 stop | NEAR | DOWN | 0.68 | 0.84 | 1.34 |
| 11-02 13:47 | +10 stop | ZEC | UP | 0.64 | 0.34 | -3.33 |
| 11-02 13:47 | +20 | ZEC | UP | 0.62 | open |  |
| 11-02 13:47 | +15 | ZEC | UP | 0.62 | open |  |
| 11-02 13:47 | +10 | ZEC | UP | 0.62 | open |  |
| 11-02 13:47 | +5 | ZEC | UP | 0.62 | open |  |
| 11-02 13:47 | +10 stop | BNB | DOWN | 0.67 | 0.77 | 0.71 |
| 11-02 13:47 | +20 | BNB | DOWN | 0.67 | 0.90 | 2.07 |
| 11-02 13:47 | +15 | BNB | DOWN | 0.68 | 0.83 | 1.29 |
| 11-02 13:47 | +10 | BNB | DOWN | 0.68 | 0.83 | 1.29 |
| 11-02 13:47 | +5 | BNB | DOWN | 0.68 | 0.74 | 0.35 |
| 11-02 13:47 | +10 stop | BTC | DOWN | 0.57 | 0.70 | 0.97 |
| 11-02 13:47 | +20 | BTC | DOWN | 0.57 | 0.81 | 2.11 |
| 11-02 13:47 | +15 | BTC | DOWN | 0.57 | 0.73 | 1.28 |
| 11-02 13:47 | +10 | BTC | DOWN | 0.57 | 0.70 | 0.97 |
| 11-02 13:47 | +5 | BTC | DOWN | 0.57 | 0.70 | 0.97 |
| 11-02 13:47 | +10 stop | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 11-02 13:47 | +10 | DOGE | DOWN | 0.57 | 0.68 | 0.76 |
| 11-02 13:47 | +5 | DOGE | DOWN | 0.57 | 0.68 | 0.76 |
| 11-02 13:47 | +10 stop | ETH | DOWN | 0.59 | 0.71 | 0.88 |
| 11-02 13:47 | +20 | ETH | DOWN | 0.59 | 0.87 | 2.55 |
| 11-02 13:47 | +15 | ETH | DOWN | 0.59 | 0.75 | 1.29 |
| 11-02 13:47 | +10 | ETH | DOWN | 0.59 | 0.71 | 0.88 |
| 11-02 13:47 | +5 | ETH | DOWN | 0.59 | 0.64 | 0.16 |
| 11-02 13:46 | +10 stop | DOGE | UP | 0.45 | 0.59 | 1.05 |
| 11-02 13:46 | +20 | DOGE | UP | 0.46 | open |  |
| 11-02 13:46 | +15 | DOGE | UP | 0.45 | open |  |
| 11-02 13:46 | +10 | DOGE | UP | 0.46 | 0.59 | 0.96 |
| 11-02 13:46 | +5 | DOGE | UP | 0.46 | 0.59 | 0.96 |
| 11-02 13:46 | +5 | HYPE | DOWN | 0.59 | 0.65 | 0.27 |
| 11-02 13:45 | +10 stop | XRP | UP | 0.56 | 0.30 | -2.93 |
| 11-02 13:45 | +20 | XRP | UP | 0.56 | open |  |
| 11-02 13:45 | +15 | XRP | UP | 0.55 | open |  |
| 11-02 13:45 | +10 | XRP | UP | 0.56 | open |  |
| 11-02 13:45 | +5 | XRP | UP | 0.57 | open |  |
| 11-02 13:45 | +10 stop | SOL | UP | 0.63 | 0.42 | -2.45 |
